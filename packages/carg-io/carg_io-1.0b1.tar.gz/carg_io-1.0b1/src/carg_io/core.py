from __future__ import annotations
from typing import List, Dict, Tuple, Generator
import pandas as pd
import numpy as np
from copy import deepcopy
import tkinter as tk
import pint
from decimal import Decimal
from pathlib import Path
import pickle

from .execeptions import SettingAttributeNotAllowed

units = ureg = pint.UnitRegistry()
NaN = np.nan


class MetaParameterSet(type):
    """Constructor type for ParameterSets."""

    def __new__(cls, clsname, bases, clsdict):

        if clsname == "ParameterSet":  # Ignore the super
            return super().__new__(cls, clsname, bases, clsdict)

        # Allocate parameter container
        parameters = []

        # Extend with parameters from super (recursive by definition)
        for base in bases:
            if hasattr(base, "_parameters"):
                parameters.extend(base._parameters)

        # Extend with own parameters

        for name, val in clsdict.items():
            import types

            if callable(val):  # isinstance(val, types.MethodType):
                # Dependent parameter
                pass
            elif not name.startswith("_"):
                # Independent parameter
                if isinstance(val, property):
                    continue  # @property may be used to create dependent Parameter
                clsdict[name] = Parameter(name, val)  # Value->Parameter substitution
                parameters.append(name)

        clsdict["_parameters"] = parameters

        # Store ParameterSet name # NOTE: may be replaced with __qualname__
        clsdict["name"] = clsname

        return super().__new__(cls, clsname, bases, clsdict)


class ParameterSet(metaclass=MetaParameterSet):
    """The ParameterSet class represents a collection of Parameter instances."""

    name: str
    _parameters: list

    LOCK_SETATTR = False

    def __init__(self):

        # Make copies of the default parameter instances
        for parm_name in self._parameters:
            parm = getattr(self, parm_name)
            setattr(self, parm_name, deepcopy(parm))
        self.LOCK_SETATTR = True

    @staticmethod
    def from_pickle(file: Path) -> ParameterSet:
        with open(file, "rb") as f:
            content: ParameterSet = pickle.load(f)
        return content

    @staticmethod
    def from_serial_pickle(data) -> ParameterSet:
        content: ParameterSet = pickle.loads(data)
        return content

    def to_dataframe(
        self, include_set_name=False, name_include_unit=False
    ) -> pd.DataFrame:
        """Return the dictionary representation of the instance.

        Parameters:
            include_set_name: bool
                If true, prepend the ParameterSet name to its Parameter names.
                This is useful when concatenating multiple ParameterSets with
                overlapping Parameter names. Default is False.
            
            name_include_unit: bool
                If True, prepend the unit in square brackets.

        """
        stack = []
        for parameter in self:
            p: pint.Quantity = parameter._value
            # value = p.m if p.m < 1 else round(p.m,2) # FIXME: does not work for arrays
            unit = format(p.u, "~").replace(" ", "")  # unit symbol without spaces
            stack.append((parameter.name, p.m, unit, parameter.is_default))

        df = pd.DataFrame(stack, columns="name value unit is_default".split())
        if include_set_name:
            df.name = (self.name + ".") + df.name

        if name_include_unit:
            df.name = df.name + " [" + df.unit + "]"

        return df

    def to_dict(self) -> Dict[str, Parameter]:
        """Return the dictionary representation of the instance."""
        return {parameter.name: parameter for parameter in self}

    def to_pickle(self, file: Path | None = None) -> Path:
        """Export the instance to a file in pickle format."""
        if not file:
            file = Path(self.name).with_suffix(".pickle")
        else:
            file = Path(file)

        with open(file, "wb") as f:
            pickle.dump(self, f)

        return file

    def __iter__(self) -> Generator[Parameter]:
        """Iterate through the parameters"""
        for parm_name in self._parameters:
            yield getattr(self, parm_name)

    def __setattr__(self, attr, value):
        if self.LOCK_SETATTR and attr in self._parameters:
            raise SettingAttributeNotAllowed(
                f"It is not allowed to set {self.name}.{attr} directly. Use {self.name}.{attr}[<unit>] = {value} instead"
            )
        object.__setattr__(self, attr, value)

    def copy(self) -> ParameterSet:
        """Return a deepcopy of self."""
        return deepcopy(self)

    def __eq__(self, other: ParameterSet) -> bool:
        return all(p == other[p.name] for p in self)

    def _to_tk(self, context, state="normal"):
        """Return as tk representation
        context: tk object - object in which to place the entries
        state: str -  can be disabled, normal, or readonly
        """
        frame = tk.LabelFrame(
            context, text=self.name, width=100, font=("Helvetica 9 bold")
        )

        entries = {}
        for row, parameter in enumerate(self):
            parameter: Parameter
            label, entry, unit = parameter._to_tk(frame)
            label.grid(row=row, column=0, padx=(2, 2), pady=(2, 2))
            entry.grid(row=row, column=1, padx=(2, 2), pady=(2, 2))
            unit.grid(row=row, column=2, padx=(2, 2), pady=(2, 2))
            entry.config(state=state)
            entries[parameter.name] = entry

        return frame, entries

    def __getitem__(self, name: str):
        dictionary = self.to_dict()
        return dictionary[name]

    def __repr__(self):
        return f"ParameterSet(name='{self.name}')"

    # def __hash__(self) -> hash:
    #     """Per default, the hash of a ParameterSet is a frozenset containing the string representation
    #     of the parameter names and their value.
    #     The unit is NOT included, hence the value should always be represented in the initial
    #     unit.
    #     """
    #     fz = []
    #     for name, parm in self.to_dict().items():
    #         fz.append(self.name + name + str(parm.normalized_value))
    #     return hash(frozenset(fz))

    def get_partial_hash(self, parameter_names: List[str]) -> hash:
        """Return the hash based on only the parameter names provided."""
        if not isinstance(parameter_names, (set, list, tuple)):
            raise TypeError(
                f"'parameter_names' must be a list, set or tuple. Got {type(parameter_names)}"
            )
        stack = []
        for name in parameter_names:
            parm = self[name]
            string = self.name + name + str(parm.normalized_value)
            stack.append(string)
        return hash(frozenset(stack))


class Parameter:
    """Parameter is typically used in context of a ParameterSet."""

    def __init__(self, name, value: pint.Quantity | float | int):
        """Create a Parameter instance with value.

        value: Either a pint.Quantity, int or float. If int or float, the value will be
                converted into a dimensionless pint.Quantity.

        """
        if not isinstance(value, pint.Quantity):
            try:
                float(value)
                value = pint.Quantity(value)  # Make dimensionless
            except Exception as err:
                raise TypeError(f"Parameter expect a number-like value, got {value}")

        self.name = name
        self._value = value
        self._unit_default = value.u  # default unit
        self.is_default = True

    @property
    def normalized_value(self) -> float | int:
        """The normalized value of a `Parameter` is the value represented in the default unit.
        Any resulting zero decimals (as result of a unit conversion) are dropper (normalized).
        """
        value = self._value.m_as(self._unit_default)
        nvalue = Decimal(value).normalize()
        return nvalue

    def __eq__(self, other: Parameter) -> bool:
        """Test if two parameters are equal. Equality is defined as having the same value
        when converted to the same unit."""
        ud = self._unit_default
        return self[ud] == other[ud]

    def __ne__(self, other: Parameter) -> bool:
        return not self == other

    def __getitem__(self, unit: str | pint.Unit) -> pint.Quantity:
        """Get the value in the requested unit. For dimensionless units, use
        Parameter[None] or Parameter[:].
        """
        if unit == None or isinstance(unit, slice):
            return self._value.m
        return self._value.m_as(unit)

    def __setitem__(self, unit: str | pint.Unit, value: float | int):
        """Set the value with the requested unit. For dimensionless units, use
        Parameter[None] or Parameter[:].
        """
        # Check dimensionality
        if not unit:
            unit = units.dimensionless
        try:
            self._value.m_as(unit)
        except pint.errors.DimensionalityError:
            raise ValueError(
                f"Trying to set {str(unit)} on parameter {self.name} that has base unit {str(self._unit_default)}"
            )

        self._value = ureg.Quantity(value, unit)
        self.is_default = False

    def _to_tk(self, root) -> Tuple[tk.Label, tk.Entry, tk.Labe]:
        """Return tkinter representation consiting of 2 labels (name and unit)
        and an entry field.

        Input:
            tkinter container entity

        Returns:
            Label(name), Entry(value), Label(unit)

        """

        name_label = tk.Label(root, text=self.name, anchor="w", width=22)

        entry = tk.Entry(root, bd=1, width=12)
        entry.insert(0, self._value.m)
        unit = str(self._value.u)
        if unit == "dimensionless":
            unit = "-"
        unit_label = tk.Label(root, text=unit, anchor="w", width=17)
        return name_label, entry, unit_label

    def __repr__(self):
        return f"Parameter(name='{self.name}'', value={self._value})"

