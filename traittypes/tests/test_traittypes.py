# encoding: utf-8
"""Tests for traittypes.traittypes."""

# Copyright (c) IPython Development Team.
# Distributed under the terms of the Modified BSD License.

from unittest import TestCase
from traitlets import HasTraits, observe
from traitlets.tests.test_traitlets import TraitTestBase
from traittypes import Array
import numpy as np


# Good / Bad value trait test cases


class IntArrayTrait(HasTraits):
    value = Array().tag(dtype=np.int)


class TestIntArray(TraitTestBase):
    """
    Test dtype validation with a ``dtype=np.int``
    """
    obj = IntArrayTrait()

    _good_values = [1, [1, 2, 3], [[1, 2, 3], [4, 5, 6]], np.array([1])]
    _bad_values = [[1, [0, 0]]]


    def assertEqual(self, v1, v2):
        return np.testing.assert_array_equal(v1, v2)


# Other test cases


class TestArray(TestCase):

    def test_array_equal(self):
        notifications = []

        class Foo(HasTraits):
            bar = Array(default_value=[1, 2])
            @observe('bar')
            def _(self, change):
                notifications.append(change)

        foo = Foo()
        foo.bar = [1, 2]
        self.assertFalse(len(notifications))
        foo.bar = [1, 1]
        self.assertTrue(len(notifications))
