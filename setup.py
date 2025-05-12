from setuptools import setup, Extension
from Cython.Build import cythonize
import sys

IS_WINDOWS = sys.platform.startswith("win")

extra_compile_args = [] if IS_WINDOWS else ["-Wno-unused-function", "-std=c++11"]

extensions = [
    Extension(
        "isf_pandas_msgpack.msgpack._packer",
        sources=["src/msgpack/_packer.pyx"],
        language="c++",
        include_dirs=["src/includes"],
        extra_compile_args=extra_compile_args,
    ),
    Extension(
        "isf_pandas_msgpack.msgpack._unpacker",
        sources=["src/msgpack/_unpacker.pyx"],
        language="c++",
        include_dirs=["src/includes"],
        extra_compile_args=extra_compile_args,
    ),
    Extension(
        "isf_pandas_msgpack._move",
        sources=["src/move.c"]
    ),
]

setup(
    ext_modules=cythonize(extensions),
)
