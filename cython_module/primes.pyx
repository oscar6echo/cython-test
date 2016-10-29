
import numpy as np

cimport cython
cimport numpy as np

from libc.math cimport sqrt

@cython.boundscheck(False)
cpdef int[:] list_primes_C(int m):
    """
    returns list of all primes up to limit_up excluded
    Sieve of Eratosthenes
    """
    cdef int i, p, k, t, sqrm, 
    cdef int[:] sieve = np.empty(m, dtype=np.int32)
    cdef int[:] primes = np.empty(m, dtype=np.int32)
    
    for i in range(m):
        sieve[i] = 1
        
    sqrm = <int>sqrt(m)
    k = 0
    for p in range(2, m):
        if sieve[p]:
            primes[k] = p;
            k += 1
            if (p<sqrm):
                t = 2*p
                while t<m:
                    sieve[t] = 0
                    t += p
                
    return primes[:k]

