Usage
=====

The ``Array`` trait type provide an implementation of a trait type for the numpy array.

``Array`` overrides certain public methods from ``TraitType`` that are generally not
 overloaded by custom trait types, in order to work around some limitations with
 numpy array comparison.

``Array`` provides an API for adding custom validators to constained proposed values for the attribute.


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

