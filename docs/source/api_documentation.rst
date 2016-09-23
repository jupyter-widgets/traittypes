API Reference Documentation
---------------------------

The ``SciType`` trait type is the base trait type for all Scipy trait types.

It complements the ``traitlets.TraitType`` with a special API to register custom
validators.

.. autoclass:: traittypes.traittypes.SciType
   :members:

The ``Array`` trait type holds a numpy Array.

.. autoclass:: traittypes.traittypes.Array

The ``DataFrame`` trait type holds a pandas DataFrame.

.. autoclass:: traittypes.traittypes.DataFrame

The ``Series`` trait type holds a pandas Series.

.. autoclass:: traittypes.traittypes.Series
