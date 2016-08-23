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

    def set(self, obj, value):
        new_value = self._validate(obj, value)
        old_value = obj._trait_values.get(self.name, self.default_value)
        obj._trait_values[self.name] = new_value
        if not np.array_equal(old_value, new_value):
            obj._notify_trait(self.name, old_value, new_value)
