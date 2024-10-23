''' This submodule has functions for calculating various optical indexes 
    including the 1D and 2D effective indexes.
'''

import numpy as np
from scipy.optimize import root_scalar

def TE_eq(beta0, k0, n1, n2, n3, slabThickness):
    ''' Need to run through a textbook at some point and remember the physical
        meaning of these parameters.
    '''
    h0 = np.sqrt( (n2 * k0)**2 - beta0**2)
    q0 = np.sqrt( beta0**2 - (n1 * k0)**2)
    p0 = np.sqrt( beta0**2 - (n3 * k0)**2)
    te0 = np.tan(h0 * slabThickness) - ((p0 + q0)/h0/(1 - (p0*q0/h0)**2))

    return (te0, h0, q0, p0)

def TM_eq(beta0, k0, n1, n2, n3, slabThickness):
    ''' Need to run through a textbook at some point and remember the physical
        meaning of these parameters.
    '''
    h0 = np.sqrt( (n2 * k0)**2 - beta0**2)
    q0 = np.sqrt( beta0**2 - (n1 * k0)**2)
    p0 = np.sqrt( beta0**2 - (n3 * k0)**2)

    pbar0 = (n2/n3)**2 * p0
    qbar0 = (n2/n1)**2 * q0

    tm0 = np.tan(h0 * slabThickness) - (h0 * (pbar0 + qbar0) / (h0**2 - pbar0 * qbar0))

    return (tm0, h0, q0, p0)

def eff_index_1D(wavelength, slabThickness, n1, n2, n3, numPoints = 1000):
    ''' Calculates all of the effective index of a (1D) slab waveguide using 
        the analytical solution to Maxwell's equations and assuming real index.

        Parameters:
         - wavelength: wavelength in meters (e.g. 1550nm as 1550e-9)
         - slabThickness: thickness of the core (n2) in meters
         - n1, n2, n3: real index of each material at the given index
         - numPoints: number of points used to search for modes; if there are
            modes spaced closer than the search range the may be missed.

        Returns: (te, tm)
         - te: list of supported TE modes
         - tm: list of supported TM modes
    '''
    k0 = 2 * np.pi / wavelength
    beta0 = np.linspace(np.max([n1, n3]) * k0, n2 * k0, 1000) 
    beta0  = beta0[:-1] # k0 * max(n1,n3) < beta < k0*n2

    # need to search the zeros of these two functions
    te0 = TE_eq(beta0, k0, n1, n2, n3, slabThickness)[0]
    tm0 = TM_eq(beta0, k0, n1, n2, n3, slabThickness)[0]

    # find TE modes
    intervals = (te0 >= 0).astype("int") - (te0 < 0).astype("int")
    zeroIndices = np.where(np.diff(intervals) < 0)[0]
    searchPoints = np.array([beta0[zeroIndices], beta0[zeroIndices+1]])
    numZeroes = len(searchPoints)

    te = []
    for index in range(numZeroes):
        bracket = (searchPoints[0, index], searchPoints[1, index])
        te.append(root_scalar(lambda x: TE_eq(x, k0, n1, n2, n3, slabThickness)[0], bracket=bracket).root/k0)

    # find TM modes
    intervals = (te0 >= 0).astype("int") - (te0 < 0).astype("int")
    zeroIndices = np.where(np.diff(intervals) < 0)[0]
    searchPoints = np.array([beta0[zeroIndices], beta0[zeroIndices+1]])
    numZeroes = len(searchPoints)
    tm = []
    for index in range(numZeroes):
        bracket = (searchPoints[0, index], searchPoints[1, index])
        tm.append(root_scalar(lambda x: TE_eq(x, k0, n1, n2, n3, slabThickness)[0], bracket=bracket).root/k0)

    return (te, tm)
