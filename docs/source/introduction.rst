.. _introduction:

Introduction
============

The `traittypes` module provides a robust reference implementation of trait
types for common data structures used in the scipy stack such as

 - `numpy <https://github.com/numpy/numpy>`_ arrays
 - `pandas <https://github.com/pydata/pandas>`_ and `xarray <https://github.com/pydata/xarray>`_ data structures

which are out of the scope of the main `traitlets <https://github.com/ipython/traitlets>`_
project but are a common requirement to build applications with traitlets in
combination with the scipy stack.

Another goal is to create adequate serialization and deserialization routines
for these trait types to be used with the `ipywidgets <https://github.com/ipython/ipywidgets>`_
project (``to_json`` and ``from_json``). These could also return a list of binary
buffers as allowed by the current messaging protocol.
