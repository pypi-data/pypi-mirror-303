import pandas as pd
import numpy as np
import inspect


class Units(object):
    """
    This class contains all Units subclasses
    - DistanceUnits
    - TimeUnits
    - FrequencyUnits
    - SpeedUnits
    - AccelerationUnits
    - PowerDensityUnits
    - EnergyDensityUnits
    - PerDistanceUnits

    """

    method: str = ""

    def __init__(self) -> None:
        """This constructor initializes Units systems"""
        if self.method == "metric":
            pass

    class DistanceUnits(object):
        """This subclass contains distance units
        - m
        - km
        - mi
        """

        m: float = 0.0
        km: float = 0.0
        mi: float = 0.0

        def __init__(self) -> None:
            """This constructor initializes m"""
            self.m = 0
            pass

        def convert_units(self) -> None:
            """This method converts DistanceUnits to km and mi"""
            self.km = self.m / 1000.0
            self.mi = self.km / 1.60934

    class TimeUnits(object):
        """This subclass contains Time units
        - s
        - min
        - h

        """

        s: float = 0.0
        min: float = 0.0
        h: float = 0.0

        def __init__(self) -> None:
            """This constructor initializes s, min, and h"""
            self.s = 0
            self.min = 0
            self.h = 0
            pass

        def convert_units(self) -> None:
            """This method converts s to min and hr"""
            self.min = self.s / 60.0
            self.h = self.min / 60.0

    class FrequencyUnits(object):
        """This subclass contains frequency units
        - Hz


        """

        hz: float = 0.0

        def __init__(self) -> None:
            """This constructor initializes FrequencyUnits"""
            pass

        def convert_units(self) -> None:
            """This method converts units. Currently no conversions"""
            # self.hz = self.min / 60.0
            pass

    class SpeedUnits(object):
        """This subclass contains Speed units
        - mps
        - kmph
        - mph
        """

        mps: float = 0.0
        kmph: float = 0.0
        mph: float = 0.0

        def __init__(self) -> None:
            """This constructor initializes mps, kmph, and mph"""
            self.mps = 0
            self.kmph = 0
            self.mph = 0
            pass

        def convert_units(self) -> None:
            """This method converts mps to kmph and mph"""
            self.kmph = self.mps * 3600 / 1000
            self.mph = self.kmph / 1.60934
            # return self.mps

    class AccelerationUnits(object):
        """This subclass contains acceleration units
        - mps2
        - kmph2
        - ftps2
        """

        mps2: float = 0.0
        kmph2: float = 0.0
        ftps2: float = 0.0

        def __init__(self) -> None:
            """This constructor initializes mps2"""
            self.mps2 = 0
            pass

        def convert_units(self) -> None:
            self.kmph2 = self.mps2 * 3600 / 1000 * 3600
            self.ftps2 = self.mps2 * 3.28084

    class PowerDensityUnits(object):
        """This subclass contains power density units
        - m2ps3

        """

        m2ps3: float = 0.0

        def __init__(self) -> None:
            """This constructor initializes PowerDensityUnits"""
            pass

        def convert_units(self) -> None:
            """This method converts m2ps3. Currently no conversions"""
            # self.kmph2 = self.mps2 / gl.KPH_2_MPS / 3600
            pass

    class EnergyDensityUnits(object):
        """This subclass contains energy density units
        - Jpkg
        """

        Jpkg: float = 0.0

        def __init__(self) -> None:
            """This constructor initializes EnergyDensityUnits"""
            pass

        def convert_units(self) -> None:
            """This constructor converts EnergyDensityUnits. Currently no conversions"""
            # self.kmph2 = self.mps2 / gl.KPH_2_MPS / 3600
            pass

    class PerDistanceUnits(object):
        """This subclass contains per distance units
        - pm
        - pkm
        - pmi

        """

        pm: float = 0.0
        pkm: float = 0.0
        pmi: float = 0.0

        def __init__(self) -> None:
            """This constructor initializes PerDistanceUnits"""
            pass

        def convert_units(self) -> None:
            """This method converts pm to pkm and pmi"""
            self.pkm = self.pm * 1000.0
            self.pmi = self.pkm * 1.60934

    def list_inner_classes(self):
        """This method returns all Units subclasses as a list

        Returns:
            list: list of Units subclasses and their arguments
        """
        units_inner_classes = [
            d
            for d in dir(Units)
            if (inspect.isclass(getattr(Units, d)) and "__" not in d)
        ]
        units_inner_class_types = [getattr(Units, d) for d in units_inner_classes]
        return units_inner_class_types
