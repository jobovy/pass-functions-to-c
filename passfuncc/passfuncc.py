# This module just contains a simple function to evaluate an arbitrary number of
# functions in C
import sys
import sysconfig
import os, os.path
import ctypes

### Load the C library ###
_ext_suffix= sysconfig.get_config_var('EXT_SUFFIX')
for path in sys.path:
    try:
        _lib = ctypes.CDLL(os.path.join(path,'passfuncc_c%s' % _ext_suffix))
    except OSError as e:
        if os.path.exists(os.path.join(path,'passfuncc_c%s' % _ext_suffix)):
            outerr= e
        _lib = None
    else:
        break
evaluate_and_add_in_c= _lib.evaluate_and_add_in_c
evaluate_and_add_in_c.argtypes= \
    [ctypes.c_double,
     ctypes.c_int,
     ctypes.c_void_p]
evaluate_and_add_in_c.restype= ctypes.c_double

def evaluate_and_add(t,*args):
    """Evaluate an arbitrary number of functions as a function of time in C,
    adds up the result from each"""
    func_ctype= ctypes.CFUNCTYPE(ctypes.c_double, # Return type
                                 ctypes.c_double) # time
    func_pyarr= [func_ctype(a) for a in args]
    func_arr = (func_ctype * len(func_pyarr))(*func_pyarr)
    return evaluate_and_add_in_c(t,len(func_pyarr),func_arr)
    