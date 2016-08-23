# Scipy Trait Types

[![Build Status](https://travis-ci.org/jupyter-incubator/traittypes.svg?branch=master)](https://travis-ci.org/jupyter-incubator/traittypes)

Trait types for NumPy, SciPy and friends

## Goals

Provide a reference implementation of trait types for common data structures used in the scipy stack such as
 - numpy arrays
 - pandas / xray data structures

which are out of the scope of the main [traitlets](https://github.com/ipython/traitlets) project but are a common requirement to build applications with traitlets in combination with the scipy stack.

Another goal is to create adequate serialization and deserialization routines for these trait types to be used with the [ipywidgets](https://github.com/ipython/ipywidgets) project (`to_json` and `from_json`). These could also return a list of binary buffers as allowed by the current message protocol. 

## Installation

For a local installation, make sure you have
[pip installed](https://pip.readthedocs.org/en/stable/installing/) and run:

```
pip install traittypes
```
