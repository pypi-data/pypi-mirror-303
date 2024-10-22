# Rapid Transformation of Lamination Parameters into Continuous Stacking Sequences

This repository holds the source code and supplementary material to the paper "Rapid Transformation of Lamination Parameters into Continuous Stacking Sequences" (add link / DOI). It consists of the layup retrieval code, lamination parameter helper functions and data visualisation code that helped us gain the discoveries mentioned in the publication (and a few more).

## Installing Dependencies / Conda Environment

The code is written Python 3. It is easiest to install all needed libraries inside a conda environment via

`
conda env create -f conda_environment.yml
`

## File Structure

`layup_search_mvp.py`

- the minimum viable example
- accesses the helper functions in `layup_search_funcs.py` and `lpfuncs.py`
- defines a lamination parameter (LP) set
- calls layup search function `search_layup()`
- prints and saves found stacking sequences to `.csv` file

`layup_search_funcs.py`

- contains the reference implementation of the solution proposal

`lpfuncs.py`

- underlying LP functions are defined in there
- sped up with numba

`dataview.py`

- plots various aspects of LP and layup space via matplotlib
- the plots can be toggled on or off via the if statement at the top of the file
- some functions require that `doe=1`

`approximate_error.py`

- How is the RMSE connected to the angle deviations to the solution?
- helps interpreting the error

`/sagemath`

- contains additional interactive visualisation tools using a SageMath Notebook

## Differences between psudo code and reference implementation

The pseudo code (Algorithm 1 in the paper) differs in some points with the reference implementation supplied here for the sake of brevity. Not all layups are kept. If the residual after optimisation is higher than some maximum allowable error, the layups are not saved. This requires a dynamic array structure.
The procedures for coordinate descent and local search can be run multiple times. This is omitted in the pseudo code. Although only one $`\Delta\theta`$ is listed as input there exist multiple to adjust different parts of the multistep algorithm. 

### What do the parameters in `search_layup()` do?

function declaration with sane default values:
`def search_layup(lps, layers, eps=0.03, error=1e-6, it_comb=100, it_sub=3, it_s=3, it_n=1, delta_doe=11.25, delta_s=3, delta_n=1, l_n=1, steps_n=3, doe=False, disp=True)`


| parameter | description |
| ------ | ------ |
| lps | target LP set that stacking sequences are searched for |
| layers | number of layers $`N`$ to search solutions in |
| eps | threshold variable $`\varepsilon`$, sets whether optimization takes place based on RMSE of the previous two steps |
| error | if the residual of the last step (local optimization) is less than this error, accept the result (stacking sequence) as a solution |
| it_comb | number of iterations / starting points, $`100`$ is quite low for difficult LP sets, set to $`>1000`$ if you cannot but should find solutions|
| it_sub | number of **s**ub iterations (how often coordinate descent and line search are repeated) |
| it_s | number of iterations for coordinate descent, one iteration always means that all $`N`$ coordinates are searched once |
| it_n | number of iterations for line search, one iteration means only one search direction is evaluated |
| delta_doe | delta angle $`\Delta\theta`$ for defining the spacing in which starting stacking sequences are generated, should not be larger than $`22.5^{\circ}`$, in degree | 
| delta_s | delta angle $`\Delta\theta`$ for defining the step length during coordinate descent, in degree |
| delta_n | delta angle $`\Delta\theta`$, step size for gradient approximation, in degree |
| steps_n | delta angle $`\Delta\theta`$ for defining the step length during line search, in degree |
| l_n | search direction length divisor during line search, 1 equals 1 length of one entire axis, 2 is half, ... ; if the entire diagonal should be searched (longer than one axis) this has to be set below $`1`$, e.g. to $`1/\sqrt{N}`$ |
| doe | set whether to use DOE (LHS) for starting point generation or random points |
| disp | toggle output of found stacking sequences during runtime |

### How to interpret the error (RMSE)?

As a rule of thumb an error of $`10^{-3}`$ represents that the angles are in sum $`\approx 1^{\circ}`$ away from the solution if $`N=12`$. The angle deviation is assumed to be distributed uniformly across all layers. For other parameters check this yourself by editing and running `approximate_error.py`.

## Getting Started

Run `layup_search_mvp.py`. It should print out found stacking sequences. They are additionally saved to a `.csv` file on disk. Modify the code to suit your needs. The comments next to the code explain most of it.


## License

GPLv3

For a copy, see LICENSE.
