# This is the main solution implementation presented in this work

import time
import numpy as np
from numba import jit
import dfols
from pyDOE import * # if LHS is used for starting point generation
from .lpfuncs import * # local module import

# define loss function for the optimizer
# DFO computes the sum of squared errors (SSE)!, This is not the MSE nor the RMSE
def loss_dfo(x, *lp_t):
    lp = get_lp(x)
    return (lp_t-lp)

# straight search along one axis at a time (coordinate descent)
@jit(nopython=True, nogil=True, cache=True, fastmath=True)
def ssearch(lam0, lps, layers, angles, modangles, iterations=1):
    # lam0 is the current best laminate, refine it and return it
    for i in range(iterations):
       k = 0 # tried angles
       while (k<layers):
           # generate all combinations for one angle
           modlams = np.repeat(lam0, angles).reshape(-1, angles).T  
           # replace all possible angles k
           modlams[:,k] = modangles
           #print(modlams)
           modlps = calc_lp_array(modlams) 
           # calc and find lowest distance value
           dists = np.sqrt(((modlps - lps)**2).sum(axis=1))
           #print(np.argmin(dists))
           min_dist = np.argmin(dists)
           # set lam0 as the one with least distance
           lam0 = modlams[min_dist]
           k = k+1
    return lam0

# search along gradient (line search)
# lam0 - current best laminate
# lps - target LPs
# delta - angle step for quasi gradient computation
# sl - search direction length divisor-> 1 equals 1 (length of entire axis), 2 is half, ...
# steps - steps in which search direction is evaluated (in DEG)
@jit(nopython=True, nogil=True, cache=True, fastmath=True)
def nearsearch(lam0, lps, layers, delta, sl, steps, iterations=1):
    for i in range(iterations):
       lp0 = get_lp(lam0)
       lam0_deg = np.rad2deg(lam0)
       # estimate gradient between solution spaces
       # generate laminates where each angle is one off (+1 grid step, equivalent to forward finite difference, although much coarser) compared to lam0 and create search direction from that
       # create quadratic stack of lam0
       modlams = np.repeat(lam0_deg, layers).reshape(-1, layers).T  
       # change only diagonal, thus get their indices [removed loop]
       # increase value in modlam by delta, wrap around if overflow occurs 
       modlams_diag = ((np.diag(modlams) + delta+90)%180)-90
       # replace modlams diagonal       
       for k in range(layers):
           modlams[k,k] = modlams_diag[k]

       modlps = calc_lp_array(np.deg2rad(modlams))
       # error of current point, eg distance
       dist = np.sqrt(((lp0 - lps)**2).sum(axis=0))
       # distance of modlams around point
       dists = np.sqrt(((modlps - lps)**2).sum(axis=1))
       # create search direction -> is already negative "gradient"
       sd = dist-dists
       # scale to [0;1] / make into unit vector
       sd = sd / np.linalg.norm(sd)
       # update lam0
       # how far to go in the search direction, max useful is diagonal of search space
       # setup search steps in np array
       searchsteps = np.arange(steps, 180//sl, steps) 
       ss_l = searchsteps.shape[0]
       # create searchlams
       searchlams = np.repeat(lam0_deg, ss_l).reshape(-1, ss_l).T  
       # create search direction array
       sd_arr = np.repeat(sd, ss_l).reshape(-1, ss_l).T  
       # calculate searchlams
       searchlams = searchlams + sd_arr * np.expand_dims(searchsteps, 1) #(searchsteps[:, np.newaxis]
       searchlams = np.deg2rad((searchlams+90)%180-90) # overflow protection, return to RAD

       searchlps = calc_lp_array(searchlams)
       # distance of searchlams 
       searchdists = np.sqrt(((searchlps - lps)**2).sum(axis=1))
       #print(searchdists)
       min_sdist = np.argmin(searchdists)
       lam0 = searchlams[min_sdist]
       return lam0

# combine both search methods and optimization
def search_layup(lps, layers, eps=0.03, error=1e-6, it_comb=100, it_sub=3, it_s=3, it_n=1, delta_doe=22.5, delta_s=3, delta_n=1, l_n=1, steps_n=3, doe=False, disp=False):
    solutions = []
    solutions_fp = [] # save full precision solutions in here
    timestamps = []
    stime = time.time() # save start time
    # generate possible angles, this is the grid to search on for ssearch (delta_s)
    # do this only once, as this computation doesn't change
    modangles = np.deg2rad(np.arange(-90+delta_s,90+delta_s,delta_s))
    angles_s = np.int32(np.floor(180/delta_s))
    # compute all start angles at once 
    # try a random start angle, should be rough -> more space filling
    # this is the minimum that covers all solution spaces
    de = delta_doe
    ang = np.int32(np.floor(180/de))
    # choose DOE or simply random start angles, no significant difference observed for low number of start values
    if doe:
        lams = np.deg2rad(np.rint(lhs(layers,it_comb)*(ang-1))*de-(90-de)).astype(np.float32)
    else:
        lams = np.random.random_sample(layers * it_comb).reshape(-1, it_comb).T.astype(np.float32)
        lams = np.deg2rad(np.rint((lams*(ang-1))*de-(90-de)))

    # go into main loop
    for k in range(it_comb):
        lam0 = lams[k] 
        # start combined search
        for i in range(it_sub):
            lam0 = ssearch(lam0, lps, layers, angles_s, modangles, it_s)
            lam0 = nearsearch(lam0, lps, layers, delta_n, l_n, steps_n, it_n)
        # calculate error (RMSE)
        err = np.sqrt(np.sum((lps-get_lp(lam0))**2)/12)#np.linalg.norm(lps-get_lp(lam0))
        #print(err)
        if err < eps: # only then do compute heavy optimization
            lbs = np.full((layers, ), np.deg2rad(-90))
            ubs = np.full((layers, ), np.deg2rad(90))
            soln = dfols.solve(loss_dfo, lam0, argsf=(lps), bounds=(lbs,ubs), maxfun=500, do_logging=False, scaling_within_bounds=True)#, rhobeg=np.deg2rad(5))
            # check if residual has been reached (confirm solution)
            # update err with RMSE first (remember, DFO-LS return the SSE!)
            err = np.sqrt(np.sum((lps-get_lp(soln.x))**2)/12)
            if err < error:
                sol = np.around(np.rad2deg(soln.x), 1).tolist()
                # don't save duplicates
                if sol not in solutions:
                    solutions.append(sol)
                    solutions_fp.append(np.rad2deg(soln.x).tolist())
                    ctime = time.time()-stime
                    timestamps.append(ctime) # how much time has passed 
                    if disp:
                        print(sol, "timestamp:", np.around(ctime,1),"s", "iter:", k)
    return np.asarray(solutions_fp), np.asarray(timestamps)
