# encoding: utf-8
"""Tests for traittypes.traittypes."""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from unittest import TestCase
from traitlets import HasTraits
from traitlets.tests.test_traitlets import TraitTestBase
from traittypes import Array
import numpy as np


class ArrayTraitTestBase(TraitTestBase):
    """A best testing class for numpy trait types.

    :meth:`assertEqual` is overloaded to not use the `__eq__` operator.
    """

    def assertEqual(self, v1, v2):
        return np.testing.assert_array_equal(v1, v2)


class IntArrayTrait(HasTraits):
    value = Array().tag(dtype=np.int)


class TestIntArray(ArrayTraitTestBase):
    """Test d-type validation with a ``dtype=np.int``."""
    obj = IntArrayTrait()

    _good_values = [1, [1, 2, 3], [[1, 2, 3], [4, 5, 6]], np.array([1])]
    _bad_values = [[1, [0, 0]]]
