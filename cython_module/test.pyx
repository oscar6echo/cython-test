
import numpy as np

from libc.math cimport exp, sqrt, pow, log


cpdef double f_C(double x):
    return x*(x+5)+np.sqrt(x)
