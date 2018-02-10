from distutils.core import setup
from Cython.Build import cythonize
setup(
    ext_modules = cythonize('i2c.pyx')
)

setup(
    ext_modules = cythonize('sensor.pyx')
)
