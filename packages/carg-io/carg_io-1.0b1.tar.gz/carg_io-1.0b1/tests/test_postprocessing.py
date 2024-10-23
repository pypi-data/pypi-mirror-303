import pytest
from pathlib import Path
from carg_io.core import Parameter, ParameterSet, units, NaN
from carg_io.postprocessing import Analyze
from random import randint
import numpy as np
import itertools


def test_post_process():
    

    class BoxI(ParameterSet):
        Length:Parameter = 1 * units.meter
        Width:Parameter = 1* units.meter
        Height:Parameter = 1* units.meter

    class BoxO(ParameterSet):
        Mass:Parameter = 1 * units.kg
        Volume:Parameter = 1 * units.meter**3
        EdgeLength:Parameter = 1 * units.meter
        SurfaceArea:Parameter = 1 * units.meter**2
        MomentOfInertiaY:Parameter = 1 * units.meter**4
        DeflectionPerkN:Parameter = 1 * units.meter

    


    def create_input_space():
        space = {
            "Length": np.linspace(2, 10, 10),
            "Width": np.linspace(2, 10, 10),
            "Height": np.linspace(2, 10, 10),
        }

        input = []
        for length, width, height in itertools.product(*space.values()):
            boxi = BoxI()
            boxi.Length['m'] = length
            boxi.Width['m'] = width
            boxi.Height['m'] = height
            input.append(boxi)
        return input

        
    def calculation(inputs):
        aaa = []
        for i in inputs:
            i:BoxI
            o = BoxO()
            l = i.Length['m']
            w = i.Width['m']
            h = i.Height['m']
            o.Volume['m**3'] = l * w * h
            o.EdgeLength['m'] = 4 * (l + w + h)
            o.Mass['kg'] = l * w * h * 7850
            o.SurfaceArea['m**2'] = 2*(l*h + h*w + w*l)
            I = o.MomentOfInertiaY['m**4'] = 1/12*w*h**3
            E = 210e9
            o.DeflectionPerkN['mm'] = 1e3*l/(48*E*I)*1e3
            aaa.append([i, o])

        return aaa
    
    design_sapce = create_input_space()
    result_space = calculation(design_sapce)

    analysis = Analyze(result_space)
    analysis.get_double_scatter(show=True)












