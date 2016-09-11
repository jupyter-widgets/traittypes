# Scipy Trait Types

[![Build Status](https://travis-ci.org/jupyter-incubator/traittypes.svg?branch=master)](https://travis-ci.org/jupyter-incubator/traittypes)
[![Documentation Status](https://readthedocs.org/projects/traittypes/badge/?version=latest)](http://traittypes.readthedocs.org/en/latest/?badge=latest)

Trait types for NumPy, SciPy and friends

## Goals

Provide a reference implementation of trait types for common data structures
used in the scipy stack such as
 - [numpy](https://github.com/numpy/numpy) arrays
 - [pandas](https://github.com/pydata/pandas) and [xarray](https://github.com/pydata/xarray) data structures

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

`traittypes` extends the `traitlets` library with an implementation of trait types for numpy arrays, pandas dataframes and pandas series.
 - `traittypes` works around some limitations with numpy array comparison to only trigger change events when necessary.
 - `traittypes` also extends the traitlets API for adding custom validators to constained proposed values for the attribute.

For a general introduction to `traitlets`, check out the [traitlets documentation](https://traitlets.readthedocs.io/en/stable/).

### Example usage with a custom validator

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

