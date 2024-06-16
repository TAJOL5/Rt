from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("RASKON", sources=["RASKON.py"]),
]

setup(
    ext_modules = cythonize(extensions),
)
