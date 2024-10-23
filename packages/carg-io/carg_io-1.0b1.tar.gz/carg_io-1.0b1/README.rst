**carg-io** is a framework facilitating parameteric analyses.
Current features are:

* Unit conversion
* Assigning default values
* Linting and autocompletion
* Quickly create parameter spaces
* Hashing
* Iteration
* Representations in `pandas.dataframe` and `tkinter`
* Visualization of input and output **ParameterSets**

Defining parameters
====================

A basic example of how to using **carg-io** is shown below using a "Box" with some input and output **ParameterSets**

.. code-block::

    from carg_io import ParameterSet, Parameter, units

    class Box(ParameterSet):
        Length:Parameter = 1 * units.meter
        Width:Parameter = 1 * units.meter
        Height:Parameter = 1 * units.meter
        Density:Parameter = 2 * units.kilogram / units.meter**3

Creating a **Box** instance and changing its values can be done by:


.. code-block::

    box = Box()
    box.Length['m'] = 2
    assert box.Length['mm'] == 2000


A simple example of 'output' of the Box and how it is calculated is show below:

.. code-block::

    class BoxOutput(ParameterSet):
        SurfaceArea:Parameter = NaN * units.meter**2
        Mass:Parameter = NaN * units.kg


    def calculation(box:Box) -> BoxOutput:
        box_out = BoxOutput()
        l = box.Length['m']
        w = box.Width['m']
        h = box.Height['m']
        box_out.SurfaceArea['m**2'] = 2 * (l*w + w*h + h*l)
        box_out.Mass['kg'] = l*w*h * box.Density['kg/m**3']
        return box_out



Default values
========

All **Parameters** have a default value.
Each **Parameter** remembers whether its value was changed (or touched) in the attribute **is_default**. 
Even setting the original default value is considered as a `change`, in the sense it was `deliberately` set.

.. code-block::

    box = Box()
    assert box.Length.is_default
    box.Length['m'] = 1
    assert not box.Length.is_default

Pandas
========

**ParameterSets** can be readily exported to a **pandas.DataFrame**.

.. code-block::

    box = Box()
    df = box.to_dataframe()
    print(df)

Dependent parameters
======


Length, Width, Height and Density are `independent`` parameters, i.e.
their value is set directly and can be readily changed.
**carg-io** also supports dependent variables (like Volume) in the following manner:

.. code-block::

    class Box(ParameterSet):
        Length:Parameter = 1 * units.meter
        Width:Parameter = 1 * units.meter
        Height:Parameter = 1 * units.meter
        Density:Parameter = 2 * units.kilogram / units.meter**3

        @property
        def Volume(self) -> Parameter:
            l = self.Length['m']
            w = self.Width['m']
            h = self.Height['m']
            return Parameter('Volume', l*w*h*units.meter**3)

Dependent parameters may be considered as an output parameters that is easily computed.



Parameter spaces
===================

Typically, an analysis will span a wide range (or "space") of values for each parameter.
**carg-io.spaces** offers functionality to achieve that quickly. A **Space** supports expanding 
and filtering the parameters in a certain direction.

.. warning::

    **Caution**: spaces have the capacity to quickly outgrow any compuation resource.
    It's important to limit the number of variations to a manageable amount.

.. code-block::

    from carg-io.spaces import Space

    space = Space(Box)
    space.expand(Box.Length, 'm', np.linspace(1,10,10))
    space.expand(Box.Width, 'm', np.linspace(1,10,10))
    space.expand(Box.Height, 'm', np.linspace(1,10,10))

    space.add_criteria("Volume", 'm**3', lambda v: v < 10*10*9)




Equality and Hashing
===========================

When dealing with multiple **ParameterSets**, equality is defined when all its **Parameters** have the same
value when converted to the same unit.


.. code-block::

    box = Box()
    box.Height['m'] = 99
    
    identical_box = Box()
    identical_box.Height['mm'] = 99_000

    hash1 = hash(box)
    hash2 = hash(identical_box)

    assert hash1 == hash2
    assert box == identical_box




It orginated as an alternative to using the python-native **dataclasses**, since **dataclasses** did not offer the
functionality 

`carg-io` supports defining, setting and bookkeeping when working with sets of parameters.
`carg-io` originated as an alternative to using the python-native `dataclass`, since `dataclasses` did not really offer the functionality needed for parametric analyses.

## Features


