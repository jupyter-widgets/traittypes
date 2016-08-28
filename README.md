# Scipy Trait Types

[![Build Status](https://travis-ci.org/jupyter-incubator/traittypes.svg?branch=master)](https://travis-ci.org/jupyter-incubator/traittypes)

Trait types for NumPy, SciPy and friends

## Goals

Provide a reference implementation of trait types for common data structures
used in the scipy stack such as
 - numpy arrays
 - pandas / xray data structures

which are out of the scope of the main [traitlets](https://github.com/ipython/traitlets)
project but are a common requirement to build applications with traitlets in
combination with the scipy stack.

Another goal is to create adequate serialization and deserialization routines
for these trait types to be used with the [ipywidgets](https://github.com/ipython/ipywidgets)
project (`to_json` and `from_json`). These could also return a list of binary
buffers as allowed by the current messaging protocol.

## Installation


Using `pip`:

Make sure you have [pip installed](https://pip.readthedocs.org/en/stable/installing/) and run:

```
pip install traittypes
```

Using `conda`:

```
conda install -c conda-forge traittypes
```

## Usage

The `Array` trait type provide an implementation of a trait type for the numpy
array.
 - `Array` overrides some methods from `TraiType` that are generally not
overloaded in order to work around some limitations with numpy array
comparison.
 - `Array` provides an API for adding custom validators to constained proposed
values for the attribute.

```python
from traitlets import HasTraits, TraitError
from traittypes import Array

def shape(*dimensions):
    def validator(trait, value):
        if value.shape != dimensions:
            raise TraitError('Expected an of shape %s and got and array with shape %s' % (dimensions, value.shape))
        else:
            return value
    return validator

class Foo(HasTraits):
    bar = Array(np.identity(2)).valid(shape(2, 2))
foo = Foo()

foo.bar = [1, 2]  # Should raise a TraitError
```

