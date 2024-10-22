#!/usr/bin/env python
"""
setup.py file """
from distutils.core import setup, Extension
#import numpy as np    

example_module = Extension('_polyclipNP',
sources=['polyclipNP_c_wrap.c', 'polyclipNP_c.c'],
)
setup (name = 'polyclipNP', version = '0.3',
author = "N. Pirzkal",
description = """Swig wrapper of polyclip.c from J.D. Smith""", 
# include_dirs = [np.get_include()], 
# ext_modules = [example_module],
py_modules = ["polyclipNP"],
)
