"""
    Dummy conftest.py for carg_io.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

import pytest
from carg_io.core import Parameter, ParameterSet, units, NaN
from carg_io.spaces import Space
import numpy as np

class Box(ParameterSet):
    Length:Parameter = 1 * units.meter
    Width:Parameter = 1* units.meter
    Height:Parameter = 1* units.meter


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

    @property
    def LengthWidthRatio(self) -> Parameter:
        l = self.Length['m']
        w = self.Width['m']
        return Parameter('LengthWidthRatio', l/w * units.dimensionless)

@pytest.fixture
def block():
    return Block()


@pytest.fixture
def block_space(block):
    space = Space(Block)
    space.expand(Block.Length, 'm', np.linspace(1,10,10))
    space.expand(Block.Width, 'm', np.linspace(1,10,10))
    space.expand(Block.Height, 'm', np.linspace(1,10,10))
    return space


class SpecializedBlock(Block):
    FilledPercentage: Parameter = 100 * units.dimensionless

    @property
    def Mass(self) -> Parameter:
        v = self.Volume['m**3']
        rho = self.Density['kg/m**3']
        f = self.FilledPercentage[None]
        return Parameter('Mass', v*rho*f * units.kg)

@pytest.fixture
def specialized_block():
    return SpecializedBlock()