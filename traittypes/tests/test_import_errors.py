
import pytest

from ..traittypes import _DelayedImportError

def test_delayed_access_raises():
    dummy = _DelayedImportError('mypackage')
    with pytest.raises(RuntimeError):
        dummy.asarray([1, 2, 3])
