from CoolProp.CoolProp import PropsSI, HAPropsSI
from tabulate import tabulate
import re
from itertools import chain

from scipy.constants import zero_Celsius


def Pressure(altitude):
    """
        Altitude above sea level.

        The pressure will be calculated by altitude above sea level according to
        ASHRAE Fundamentals Handbook.

        :param value: The value of the input [m].
        :return: Altitude above sea level for the input.
        :raises ValueError: If altitude above sea level is not between
            -5000 and 11000 meters.
        """
    if not -5000 <= altitude <= 11000:
        raise ValueError(
            "Altitude above sea level should be between -5000 and 11000 meters!"
            )
    return 101325 * (1 - 2.25577e-5 * altitude) ** 5.25588

class Temperature:
        """содержит температуру в кельвинах или градусах Цельсия"""
        class _Kelvin:
                def __get__(self, obj, cls):
                        try:
                                obj.__dict__["T"] = obj.__dict__["t"]  + zero_Celsius
                        except KeyError: pass
                        return obj.__dict__["T"]
                
                def __set__(self, obj, val):
                        assert isinstance(val, (int, float)), f"inNumber is neither int nor float, it is {type(val)}"
                        obj.__dict__['T'] = val
        class _Celsius:
                def __get__(self, obj, cls):
                        try:
                                obj.__dict__["t"] = obj.__dict__["T"] - zero_Celsius
                        except KeyError: pass
                        return obj.__dict__["t"]
                def __set__(self, obj, val):
                        assert isinstance(val, (int, float)), f"inNumber is neither int nor float, it is {type(val)}"
                        obj.__dict__['t'] = val
        t = _Celsius()
        T = _Kelvin()
        def __init__(self, *, t=None, T=None):
                assert t is None or T is None, "only one 't' or 'T' is required"
                if t is not None:
                        self.t = t
                if T is not None:
                        self.T = T

class HUAir:
    def __init__(self, **inputs):
        self._inputs = tuple(chain.from_iterable(sorted(inputs.items())))

    def __getattr__(self, attr):
        self.__dict__[attr] = HAPropsSI(*((attr,) + self._inputs))
        return self.__dict__[attr]
    @property
    def density(self) -> float: #повзаимствовано у PyFluids
        """Mass density per humid air unit [kg/m3]."""
        return 1 / self.Vha


#Eurovent Reference design temperatures
#Operating conditions for standard rating:
#Comfort Air Conditioner - Cooling mode

p00_indoor_unit = {
        "Cooling": {'T':Temperature(t=27).T,'P':101325,'Twb':Temperature(t=19).T},
        "Heating": {'T':Temperature(t=20).T,'P':101325,'Twb':Temperature(t=15).T}
                }

p00_outdoor_unit = {
        "Cooling": {'T':Temperature(t=35).T,'P':101325,'Twb':Temperature(t=24).T},
        "Heating": {'T':Temperature(t=7).T,'P':101325,'Twb':Temperature(t=6).T}
                }

p01 = HUAir(**p00_indoor_unit["Cooling"])       #готовые точки p01 для условий Eurovent
p02 = HUAir(**p00_indoor_unit["Heating"])       #готовые точки p02       

p11 = HUAir(**p00_outdoor_unit["Cooling"])       #готовые точки p11
p12 = HUAir(**p00_outdoor_unit["Heating"])       #готовые точки p12

def pprint(humidairpoints: HUAir, parameter=None): #именно этот
    parameters_map = {'B' : 'B', 'Twb' : 'B', 'T_wb' : 'B', 'WetBulb ' : 'B',
                      'C' : 'cp', 'cp ' : 'cp',
                      'Cha' : 'Cha', 'cp_ha ' : 'Cha',
                      'D' : 'D', 'Tdp' : 'D', 'DewPoint' : 'D', 'T_dp ' : 'D',
                      'H' : 'H', 'Hda' : 'H', 'Enthalpy' : 'H',
                      'Hha' : 'Hha',
                      'K' : 'k', 'k' : 'k', 'Conductivity ' : 'k',
                      'M' : 'mu', 'Visc' : 'mu', 'mu ' : 'mu',
                      'psi_w' : 'Y', 'Y ' : 'Y',
                      'P' : 'P',
                      'P_w' : 'P_w',
                      'R' : 'R', 'RH' : 'R', 'RelHum ' : 'R',
                      'S' : 'S', 'Sda' : 'S', 'Entropy ' : 'S',
                      'Sha ' : 'Sha',
                      'T' : 'T', 'Tdb' : 'T', 'T_db ' : 'T',
                      'V' : 'V', 'Vda ' : 'V',
                      'Vha ' : 'Vha',
                      'W' : 'W', 'Omega' : 'W', 'HumRat ' : 'W',
                      'Z ' : 'Z',
                      'density': 'density', 'Density': 'density'}

    parameters_desc = {'B' : ('K', 'Wet-Bulb Temperature'),
                       'cp' : ('J/kg dry air/K', 'Mixture specific heat per unit dry air'),
                       'Cha' : ('J/kg humid air/K', 'Mixture specific heat per unit humid air'),
                       'D' : ('K', 'Dew-Point Temperature'),
                       'H' : ('J/kg dry air', 'Mixture enthalpy per dry air'),
                       'Hha' : ('J/kg humid air', 'Mixture enthalpy per humid air'),
                       'k' : ('W/m/K', 'Mixture thermal conductivity'),
                       'mu' : ('Pa-s', 'Mixture viscosity'),
                       'Y' : ('mol water/mol humid air', 'Water mole fraction'),
                       'P' : ('Pa', 'Pressure'),
                       'P_w' : ('Pa', 'Partial pressure of water vapor'),
                       'R' : ('', 'Relative humidity in [0, 1]'),
                       'S' : ('J/kg dry air/K ', 'Mixture entropy per unit dry air'),
                       'Sha' : ('J/kg humid air/K ', 'Mixture entropy per unit humid air'),
                       'T' : ('K', 'Dry-Bulb Temperature'),
                       'V' : ('m³/kg dry air', 'Mixture volume per unit dry air'),
                       'Vha' : ('m³/kg humid air', 'Mixture volume per unit humid air'),
                       'density': ('kg/m³ humid air', "Mass density per humid air unit"),
                       'W' : ('kg water/kg dry air', 'Humidity Ratio'),
                       'Z' : ('', 'Compressibility factor (Z=pv/(RT))')
                       }
    #data = [ (parameters_desc[parameters_map[param]][1], parameters_desc[parameters_map[param]][0], getattr(humidair, param) ) for param in ("P", "T", "R", "Twb", "Hda", "Hha", "W", "DewPoint", "density", "P_w")]
    if isinstance(humidairpoints, HUAir): humidairpoints = (humidairpoints, )
    data = []
    parameters = ("P", "T", "R", "Twb", "Hda", "Hha", "W", "DewPoint", "density", "P_w")
#    if parameter is None:            
    if parameter in parameters_map: parameters = parameters + (parameter,)
    for param in parameters:
            _ = (parameters_desc[parameters_map[param]][1],
                    parameters_desc[parameters_map[param]][0],
                    )
            for humidair in humidairpoints:
                    _ = _ + (getattr(humidair, param),)
            data.append(_)
                    
    print(tabulate(data, tablefmt="plain"))
