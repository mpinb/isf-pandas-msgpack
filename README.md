# isf-pandas-msgpack

[![CI](https://github.com/mpinb/isf-pandas-msgpack/actions/workflows/ci.yml/badge.svg)](https://github.com/mpinb/isf-pandas-msgpack/actions/workflows/ci.yml)
[![Build](https://github.com/mpinb/isf-pandas-msgpack/actions/workflows/build.yml/badge.svg)](https://github.com/mpinb/isf-pandas-msgpack/actions/workflows/build.yml)
[![PyPI](https://github.com/mpinb/isf-pandas-msgpack/actions/workflows/publish.yml/badge.svg)](https://pypi.org/project/isf-pandas-msgpack/)

**pandas-msgpack** is an interface to msgpack for pandas. It allows for convenient IO of common pandas objects to the `msgpack` format, 
including performant compression like `blosc`.

This package is a fork of the original `pandas-msgpack`, which has not been maintained since
its inception in 2017 by the PyData team. However, it is to date an extremely performant dataformat.

We are not the original authors of this package, and we do not claim any ownership of the original code. 
We are simply maintaining and updating it for use in our main project ISF (https://github.com/mpinb/in_silico_framework).
We have no interest in adding new features, or making this broadly applicable. PRs are however very welcome.

## Installation

Install latest release version via pip

```shell
pip install isf-pandas-msgpack
```
