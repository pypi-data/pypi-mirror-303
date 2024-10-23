from setuptools import setup, Extension
import numpy

try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = {}
ext_modules = []

if use_cython:
    ext_modules += [
        Extension("pyMPPost.cython_functs", ["src/pyMPPost/cython_functs.pyx"],define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
        include_dirs=[numpy.get_include()]),
    ]
    cmdclass.update({'build_ext': build_ext})
else:
    ext_modules += [
        Extension("pyMPPost.cython_functs", ["src/pyMPPost/cython_functs.c"]),
    ]

setup(
    name='pyMPPost',
    cmdclass=cmdclass,
    ext_modules=ext_modules,
)