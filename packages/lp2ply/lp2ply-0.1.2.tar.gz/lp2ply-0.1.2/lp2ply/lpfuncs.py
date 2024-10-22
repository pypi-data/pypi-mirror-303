# utility functions for generating layups, computing LP and gradients
# made faster with numba    

import numpy as np
from numba import jit

# this generates the combination at any place in the lp space, so no need to save them all
# input angles are in DEG! Valid Range from ]-90°;90°]
# index: each layup has a specific integer that descibes it -> number lock principle
# layers: number of layers N
# angle_size: number of angles K (eg. 4 if only [-45°, 0°, 45°, 90°] are permitted)
# delta: reverse of angle_size (eg. 45° even spacing of angles) -> DUPLICATION!
# offset: where to start applying the delta, don't start at -90°, but at -90°+offset
@jit(nopython=True, nogil=True, cache=True, fastmath=False)
def get_combination(index, layers, delta, offset=0):
    # cast to ints for numba
    layers = np.int32(layers)
    angle_size = np.int32(np.floor(180/delta)) # compute number of angles from given delta
    # start combination generation, use number lock like method, where the angle in each layer increases step by step (implemented via modulo)
    # the angle in the first layer moves the fastest
    ia = np.arange(0, layers)
    la = np.full((layers,), angle_size)
    # array of indices of angles[], scaled to fit into ]-90°;90°]
    aia = np.mod(np.floor_divide(index, la**ia),la)*delta-(90-delta+offset)
    return np.deg2rad(aia) # convert to radians  
    # non numpy variant (slower, but easier to understand) 
    #return np.array([angles[((index // (l**i)) % l)] for i in range(lam.size)], dtype='int8')

# lam: layup of laminate, as a numpy array, angles in RADIANS
# see Aeroelastic Design of Blended Composite Structures Using Lamination Parameters, Macquart et al. , 2017 for reference
@jit(nopython=True, nogil=True, cache=True, fastmath=False)
def get_lp(lam):
    #laminate contains the angles, length is the number of layers N
    N = lam.size
    # empty return array for 12 LP
    lp = np.zeros((12,), dtype=np.float32) 
    # angle arrays
    lam2 = lam*2
    lam4 = lam*4
    cos2 = np.cos(lam2).astype(np.float32) #numba doesn't support ints, ensure these are floats!
    cos4 = np.cos(lam4).astype(np.float32)
    sin2 = np.sin(lam2).astype(np.float32)
    sin4 = np.sin(lam4).astype(np.float32)
    # Z arrays
    Z2 = np.array([((-N/2+i+1)**2 -(-N/2+i)**2) for i in range(N)]).astype(np.float32)
    Z3 = np.array([((-N/2+i+1)**3 -(-N/2+i)**3) for i in range(N)]).astype(np.float32)
    #combine them
    # in plane 
    lp[0] = np.sum(cos2)/N
    lp[1] = np.sum(sin2)/N
    lp[2] = np.sum(cos4)/N
    lp[3] = np.sum(sin4)/N
    # coupled
    N2 = 2/(N**2)
    lp[4] = np.dot(Z2, cos2)*N2 
    lp[5] = np.dot(Z2, sin2)*N2 
    lp[6] = np.dot(Z2, cos4)*N2 
    lp[7] = np.dot(Z2, sin4)*N2 
    # out of plane
    N3 = 4/(N**3)
    lp[8] = np.dot(Z3, cos2)*N3
    lp[9] = np.dot(Z3, sin2)*N3 
    lp[10] = np.dot(Z3, cos4)*N3 
    lp[11] = np.dot(Z3, sin4)*N3
    return lp

# analytically derived jacobian -> check this before using it!
@jit(nopython=True, nogil=True, cache=True, fastmath=False)
def get_lp_jac(lam):
    #laminate contains the angles, length is the number of layers N, input is RADIANS!
    N = lam.size
    # empty return jacobian array for Nx12 LP gradients
    grad = np.zeros((N, 12), dtype=np.float32)
    # angle arrays
    lam2 = lam*2
    lam4 = lam*4
    cos2 = np.cos(lam2).astype(np.float32) #numba doesnt support ints, ensure those are floats!
    cos4 = np.cos(lam4).astype(np.float32)
    sin2 = np.sin(lam2).astype(np.float32)
    sin4 = np.sin(lam4).astype(np.float32)
    # Z arrays
    Z2 = np.array([((-N/2+i+1)**2 -(-N/2+i)**2) for i in range(N)]).astype(np.float32)
    Z3 = np.array([((-N/2+i+1)**3 -(-N/2+i)**3) for i in range(N)]).astype(np.float32)
    #combine them
    # in plane 
    grad[:,0] = -sin2*2/N
    grad[:,1] = cos2*2/N
    grad[:,2] = -sin4*4/N
    grad[:,3] = cos4*4/N
    # coupled
    N2 = 2/(N**2)
    grad[:,4] = -sin2*2*Z2*N2
    grad[:,5] = cos2*2*Z2*N2
    grad[:,6] = -sin4*4*Z2*N2
    grad[:,7] = cos4*4*Z2*N2
    # out of plane
    N3 = 4/(N**3)
    grad[:,8] = -sin2*2*Z3*N3
    grad[:,9] = cos2*2*Z3*N3
    grad[:,10] = -sin4*4*Z3*N3
    grad[:,11] = cos4*4*Z3*N3
    return grad

# analytically derived hessian -> check this before using it!
@jit(nopython=True, nogil=True, cache=True, fastmath=False)
def get_lp_hess_diag(lam):
    #laminate contains the angles, length is the number of layers N, input is RADIANS!
    N = lam.size
    # empty return Hessian array for NxNx12 LP second order gradients
    #hess = np.zeros((N, N, 12), dtype=np.float32)
    # second order non zero gradients (main diagonals in hessian)
    grad2 = np.zeros((N, 12), dtype=np.float32)
    # angle arrays
    lam2 = lam*2
    lam4 = lam*4
    cos2 = np.cos(lam2).astype(np.float32) #numba doesnt support ints, ensure those are floats!
    cos4 = np.cos(lam4).astype(np.float32)
    sin2 = np.sin(lam2).astype(np.float32)
    sin4 = np.sin(lam4).astype(np.float32)
    # Z arrays
    Z2 = np.array([((-N/2+i+1)**2 -(-N/2+i)**2) for i in range(N)]).astype(np.float32)
    Z3 = np.array([((-N/2+i+1)**3 -(-N/2+i)**3) for i in range(N)]).astype(np.float32)
    #combine them
    # in plane 
    grad2[:,0] = cos2*-4
    grad2[:,1] = sin2*-4
    grad2[:,2] = cos4*-16
    grad2[:,3] = sin4*-16
    # coupled
    N2 = 2/(N**2)
    grad2[:,4] = grad2[:,0]*Z2*N2
    grad2[:,5] = grad2[:,1]*Z2*N2
    grad2[:,6] = grad2[:,2]*Z2*N2
    grad2[:,7] = grad2[:,3]*Z2*N2
    # out of plane
    N3 = 4/(N**3)
    grad2[:,8] = grad2[:,0]*Z3*N3
    grad2[:,9] = grad2[:,1]*Z3*N3
    grad2[:,10] = grad2[:,2]*Z3*N3
    grad2[:,11] = grad2[:,3]*Z3*N3
    # blow second order gradient vectors up into matrix NxN, write into hessian
    #hess[:,:,0] = np.diag(grad2[:,0])   
    #hess[:,:,1] = np.diag(grad2[:,1])   
    #hess[:,:,2] = np.diag(grad2[:,2])   
    #hess[:,:,3] = np.diag(grad2[:,3])   
    #hess[:,:,4] = np.diag(grad2[:,4])   
    #hess[:,:,5] = np.diag(grad2[:,5])   
    #hess[:,:,6] = np.diag(grad2[:,6])   
    #hess[:,:,7] = np.diag(grad2[:,7])   
    #hess[:,:,8] = np.diag(grad2[:,8])   
    #hess[:,:,9] = np.diag(grad2[:,9])   
    #hess[:,:,10] = np.diag(grad2[:,10])   
    #hess[:,:,11] = np.diag(grad2[:,11])   
    #det = np.prod(grad2, axis=0) # not supported by numba, do it in numpy on return instead
    return grad2 # or just return the matrix diagional as a single vector

@jit(nopython=True, nogil=True, cache=True)
def calc_lp_array_jit(inp, layers, delta, offset=0, block_id=None):
    #block_id gets magically passed by map_blocks func
    #print(block_id)
    #print(inp.shape)
    angle_size = np.int32(np.floor(180/delta)) # compute number of angles from given delta
    outp = np.empty_like(inp)
    l_pos = inp.shape[0]*block_id[0] # local block start pos in whole array
    for i in range(inp.shape[0]):
        comb = get_combination(i+l_pos, layers, delta, offset)
        outp[i] = get_lp(comb)
    return outp
# calc lps of multiple laminates
@jit(nopython=True, nogil=True, cache=True)
def calc_lp_array(inp):
    outp = np.zeros((inp.shape[0],12), dtype=np.float32) 
    for i in range(inp.shape[0]):
        outp[i] = get_lp(inp[i])
    return outp

@jit(nopython=True, nogil=True, cache=True)
def calc_lp_jac_array_doe(inp):
    # outp has shape [samples, layers, lp_gradient]
    outp = np.zeros((inp.shape[0], inp.shape[1], 12), dtype=np.float32) 
    for i in range(inp.shape[0]):
        outp[i] = get_lp_jac(inp[i])
    return outp

# calculate RMSE of multiple passed in lps compared to a reference lp
@jit(nopython=True, nogil=True, cache=True)
def calc_lp_array_RMSE(inp, reflp):
    outp = np.zeros((inp.shape[0],), dtype=np.float32) 
    for i in range(inp.shape[0]):
        # RMSE
        outp[i] = np.sqrt(((reflp - inp[i])**2).sum(axis=0)/12)
    return outp

@jit(nopython=True, nogil=True, cache=True, fastmath=False)
def get_comb_array(lay, layers, delta):
    angle_size = np.int32(np.floor(180/delta)) # compute number of angles from given delta
    comb = angle_size**layers
    outp = np.zeros((comb, ))
    for i in range(comb):
        ia = np.arange(0, layers)
        la = np.full((layers,), angle_size)
        aia = np.mod(np.floor_divide(i, la**ia),la)*delta-(90-delta)
        outp[i] = aia[lay]
    return outp 
