from setuptools import setup, Extension
from Cython.Build import cythonize
import sys

IS_WINDOWS = sys.platform.startswith("win")

extra_compile_args = [] if IS_WINDOWS else ["-Wno-unused-function", "-std=c++11"]

extensions = [
    Extension(
        "isf_pandas_msgpack.msgpack._packer",
        sources=["isf_pandas_msgpack/msgpack/_packer.pyx"],
        language="c++",
        include_dirs=["isf_pandas_msgpack/includes"],
        extra_compile_args=extra_compile_args,
    ),
    Extension(
        "isf_pandas_msgpack.msgpack._unpacker",
        sources=["isf_pandas_msgpack/msgpack/_unpacker.pyx"],
        language="c++",
        include_dirs=["isf_pandas_msgpack/includes"],
        extra_compile_args=extra_compile_args,
    ),
    Extension(
        "isf_pandas_msgpack._move",
        sources=["isf_pandas_msgpack/move.c"]
    ),
]

setup(
    ext_modules=cythonize(extensions),
)
