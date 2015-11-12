from traitlets import TraitType, TraitError
import numpy as np


class Array(TraitType):

    """A numpy array trait type."""

    info_text = 'a numpy array'

    def validate(self, obj, value):
        try:
            return np.asarray(value, dtype=self.get_metadata('dtype'),
                              order=self.get_metadata('order'))
        except (ValueError, TypeError) as e:
            raise TraitError(e)
