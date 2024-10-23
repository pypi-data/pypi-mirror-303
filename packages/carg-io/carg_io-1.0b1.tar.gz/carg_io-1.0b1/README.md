# Carg-io

`carg-io` helps ease working with sets of parameters.
Specifically, in the field of engineering: if it's worth automating, it's worth parametrizing.
This means that *if* you tackled the hard part (finding and programming a solution), it would be a shame to get lost in all your input and output. I/O should be just cargo.


## Features

**Essentials**
- Defining parameter sets
- Support units
- Checking if a default value was changed
- Checking parameter set equality
- Defining dependent parameters

**Export and visualization**
- Visualizing input/output parameter sets
- Export and load from conventional formats (pandas DataFrame)
- Tkinter representation

`carg-io` originated as an alternative to using the python-native `dataclass`, since `dataclasses` did not really offer the functionality needed for parametric analyses.

## Basic use

### Definition and creation
Below an example of how to organize the parameters for a `block` object.


```python
from carg_io import ParameterSet, Parameter, units

class Block(ParameterSet):
    Length:Parameter = 1 * units.meter
    Width:Parameter = 1 * units.meter
    Height:Parameter = 1 * units.meter
    Density:Parameter = 2 * units.kilogram / units.meter**3
```

`Block` is a set of 4 Parameters with each a default value and a default unit.
Using this structure will allow typical IDEs to auto-complete the namespaces, allowing for faster development.

When making an instance of `Block`, it will always be created with default values.
They can be changed at will after. When changing (=setting) a parameter, always specify the unit in square brackets:

```python
block = Block()
block.Length['m'] = 2
```

Similarly, getting the current value of a parameter *also* requires a unit:

```python
l = block.Length['foot']
print(f"Length in foot is: {l}")
```

### Dimensionless parameters
Units *have to be specified* when getting of setting Parameter values.
Imagine `Block` would have a length/width ratio Parameter. In this case you should use `None` to indicate the dimensionless unit:

```python
class Block(ParameterSet):
    LengthWidthRatio = 1 * units.dimensionless

block.LengthWidthRatio[None] = 1.2
print(block.LengthWidthRatio[None])

```

Alternatively, using `:` is also supported:

```python
block.LengthWidthRatio[:] = 1.2
print(block.LengthWidthRatio[:])

```


### Parametrization

Parametrizing an analysis can be done using standard iteration tools, e.g.:

```python
from itertools import product

# Generate a bunch of parameter set instances
blocks = []
for l, w, h in product([1,2,3], [1,2,3], [1,2,3]):
    block = Block()
    block.Length["m"] = l
    block.Width["m"] = w
    block.Height["m"] = h
    blocks.append(block)

# For each parameters set, perform a calculation
for block in blocks:
    wall_area = \
        2 * block.Length["m"] * block.Height["m"] + \
        2 * block.Width["m"] * block.Height["m"] + \
    print(wall_area)

```

Be aware though that combinations like these tend to grow very quickly.
After the problem is properly automated, there is wisdom in *what* to analyze exactly.


### Dependent parameters
Typical parameters are *independent*, i.e. they are at the core of what defines a `Block`.
In the example below, `Block.Volume` and `Block.Mass` are *dependent* parameters, in that theya are fully defined by the length, width, height and density of the block.

```python
from carg_io import ParameterSet, Parameter, units

class Block(ParameterSet):
    Length:Parameter = 1 * units.meter
    Width:Parameter = 1 * units.meter
    Height:Parameter = 1 * units.meter
    Density:Parameter = 2 * units.kilogram / units.meter**3

    @property
    def Volume(self) -> Parameter:
        l = self.Length['m']
        w = self.Width['m']
        h = self.Height['m']
        return Parameter('Volume', l*w*h * units.meter**3)

    @property
    def Mass(self) -> Parameter:
        v = self.Volume['m**3']
        rho = self.Density['kg/m**3']
        return Parameter('Mass', v*rho * units.kg)

```

This ensures that, even though volume and mass are not essential characteristic of Block, they are conveniently available.

```python
block = Block()
block.Length['m'] = 2
assert block.Mass['t'] == 2000

```

### Spaces

Taking the parametrization one step further, we introduce `Space`.

```python
s = Space(Block)
s.expand(Block.Length, "m", [1,2,3])
s.expand(Block.Width, "m", [1,2,3])
s.expand(Block.Height, "m", [1,2,3])
assert len(s) == 9

```
Note that `Space` accepts a *class*, not an *instance*.

#### Criteria
At times, it's conveniet to filter spaces based on some characteristic.
It would be a bit illogical to filter based on a value of an independent parameters; just do not expand it beyond the criteria. But filtering based on *dependent* parameters *does* make sense.

```python
s = Space(Block)
s.expand(Block.Length, "m", [1,2,3])
s.expand(Block.Width, "m", [1,2,3])
s.expand(Block.Height, "m", [1,2,3])
s.expand(Block.Density, "m", [2])
s.add_criteria(Block.Mass, "kg", lambda m: m < 54)

assert len(s) == 26
```
In the example above, the largest block is 3x3x3 and has a mass of 54 kg.
The criteria will filter out this block, and hence, the number of parameter sets represented in the space is 26.


<!-- #### Uniformity
In the previous section, we discarded a single parameter set.
This means that, even though the space was initially expanded linearly in all directions (a uniform space), it no longer is.
This has implications for your results, e.g. it may lead to survivor bias. -->



## No categorical data
Categorical data, such as as choice between `GREEN`, `BLUE`, `YELLOW`, is deliberately not supported.
The reason for this is that `carg-io` focusses on numerical values only, since only numerical values can be shown in a graph.

Typically, digging deeper into categorical values, one will eventually find numerical values again. E.g. the colors `GREEN`, `BLUE` and `YELLOW` are actually wave lenghts 550, 450 and 580 nm.


