Usage
=====

Example: Validating the Shape of a Numpy Array
----------------------------------------------

We pass a validation function to the ``valid`` method of the ``Array`` trait type.

In this example, the validation function is returned by the ``shape`` closure which stores
the tuple in its closure.

.. code::

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
