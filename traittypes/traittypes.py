from traitlets import TraitType, TraitError, Undefined
import numpy as np


class Array(TraitType):

    """A numpy array trait type."""

    info_text = 'a numpy array'
    dtype = None

    def validate(self, obj, value):
        if value is None and not self.allow_none:
            self.error(obj, value)
        try:
            value = np.asarray(value, dtype=self.dtype)
            for validator in self.validators:
                value = validator(self, value)
            return value
        except (ValueError, TypeError) as e:
            raise TraitError(e)

    def set(self, obj, value):
        new_value = self._validate(obj, value)
        old_value = obj._trait_values.get(self.name, self.default_value)
        obj._trait_values[self.name] = new_value
        if not np.array_equal(old_value, new_value):
            obj._notify_trait(self.name, old_value, new_value)

    def __init__(self, default_value=Undefined, allow_none=False, dtype=None, **kwargs):
        self.dtype = dtype
        if default_value is Undefined:
            default_value = np.array(0, dtype=self.dtype)
        elif default_value is not None:
            default_value = np.asarray(default_value, dtype=self.dtype)
        self.validators = []
        super(Array, self).__init__(default_value=default_value, allow_none=allow_none, **kwargs)

    def valid(self, *validators):
        """
        Register new trait validators

        Validators are functions that take two arguments.
         - The trait instance
         - The proposed value

        Validators return the (potentially modified) value, which is either
        assigned to the HasTraits attribute or input into the next validator.

        They are evaluated in the order in which they are provided to the `valid`
        function.

        Example
        -------

        .. code-block:: python
            # Test with a shape constraint
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
        """
        self.validators.extend(validators)
        return self
