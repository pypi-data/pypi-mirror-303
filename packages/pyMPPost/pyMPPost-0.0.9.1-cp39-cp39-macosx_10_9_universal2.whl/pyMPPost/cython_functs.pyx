import numpy as np
cimport numpy as cnp
cimport cython

cnp.import_array()

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
@cython.initializedcheck(False)
cpdef calc_pulses(long[:] history, long[:] cell, double[:] time, long[:] detector_mat, double[:] pgt_arr, double[:] dt_arr, double tol):
    cdef Py_ssize_t N = len(history)
    cdef double begin
    cdef long curr_pulse = 0
    cdef long curr_detect = -1
    cdef long curr_hist = -1

    cdef Py_ssize_t k
    pulses = np.zeros(N, dtype=long)
    cdef long[::1] pulses_view = pulses
    
    for k in range(N):
        if curr_hist != history[k] or curr_detect != cell[k]:
            curr_hist = history[k]
            curr_detect = cell[k]
            curr_pulse = 0
            begin = time[k]
            mat_num = detector_mat[k]
            pgt = pgt_arr[mat_num]
            dt = dt_arr[mat_num]

        
        if (time[k] - begin) - pgt <= tol:
            pulses_view[k] = curr_pulse
        elif (time[k] - begin) - (pgt+dt) > tol:
            begin = time[k]
            curr_pulse += 1
            pulses_view[k] = curr_pulse
        else:
            pulses_view[k] = -1
    return pulses
    