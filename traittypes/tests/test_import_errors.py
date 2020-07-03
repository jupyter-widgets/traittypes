
from unittest import TestCase

from ..traittypes import _DelayedImportError


class TestError(TestCase):
    def test_delayed_access_raises(self):
        dummy = _DelayedImportError('mypackage')
        with self.assertRaises(RuntimeError):
            dummy.asarray([1, 2, 3])
