#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  HEOSProps.py
#
#  @Copyright: 2018 by iop <iop@com.ny>
#
#  @license: GNU GPL, see COPYING for details.

"""
Doc this module

samples this module
"""

from CoolProp.CoolProp import PropsSI

a = """DELTA, Delta 	  	IO 	False 	Reduced density (rho/rhoc)
DMOLAR, Dmolar 	mol/m^3 	IO 	False 	Molar density
D, DMASS, Dmass 	kg/m^3 	IO 	False 	Mass density
HMOLAR, Hmolar 	J/mol 	IO 	False 	Molar specific enthalpy
H, HMASS, Hmass 	J/kg 	IO 	False 	Mass specific enthalpy
P 	Pa 	IO 	False 	Pressure
Q 	mol/mol 	IO 	False 	Mass vapor quality
SMOLAR, Smolar 	J/mol/K 	IO 	False 	Molar specific entropy
S, SMASS, Smass 	J/kg/K 	IO 	False 	Mass specific entropy
TAU, Tau 	  	IO 	False 	Reciprocal reduced temperature (Tc/T)
T 	K 	IO 	False 	Temperature
UMOLAR, Umolar 	J/mol 	IO 	False 	Molar specific internal energy
U, UMASS, Umass 	J/kg 	IO 	False 	Mass specific internal energy
ACENTRIC, acentric 	  	O 	True 	Acentric factor
ALPHA0, alpha0 	  	O 	False 	Ideal Helmholtz energy
ALPHAR, alphar 	  	O 	False 	Residual Helmholtz energy
A, SPEED_OF_SOUND, speed_of_sound 	m/s 	O 	False 	Speed of sound
BVIRIAL, Bvirial 	  	O 	False 	Second virial coefficient
CONDUCTIVITY, L, conductivity 	W/m/K 	O 	False 	Thermal conductivity
CP0MASS, Cp0mass 	J/kg/K 	O 	False 	Ideal gas mass specific constant pressure specific heat
CP0MOLAR, Cp0molar 	J/mol/K 	O 	False 	Ideal gas molar specific constant pressure specific heat
CPMOLAR, Cpmolar 	J/mol/K 	O 	False 	Molar specific constant pressure specific heat
CVIRIAL, Cvirial 	  	O 	False 	Third virial coefficient
CVMASS, Cvmass, O 	J/kg/K 	O 	False 	Mass specific constant volume specific heat
CVMOLAR, Cvmolar 	J/mol/K 	O 	False 	Molar specific constant volume specific heat
C, CPMASS, Cpmass 	J/kg/K 	O 	False 	Mass specific constant pressure specific heat
DALPHA0_DDELTA_CONSTTAU, dalpha0_ddelta_consttau 	  	O 	False 	Derivative of ideal Helmholtz energy with delta
DALPHA0_DTAU_CONSTDELTA, dalpha0_dtau_constdelta 	  	O 	False 	Derivative of ideal Helmholtz energy with tau
DALPHAR_DDELTA_CONSTTAU, dalphar_ddelta_consttau 	  	O 	False 	Derivative of residual Helmholtz energy with delta
DALPHAR_DTAU_CONSTDELTA, dalphar_dtau_constdelta 	  	O 	False 	Derivative of residual Helmholtz energy with tau
DBVIRIAL_DT, dBvirial_dT 	  	O 	False 	Derivative of second virial coefficient with respect to T
DCVIRIAL_DT, dCvirial_dT 	  	O 	False 	Derivative of third virial coefficient with respect to T
DIPOLE_MOMENT, dipole_moment 	C m 	O 	True 	Dipole moment
FH 	  	O 	True 	Flammability hazard
FRACTION_MAX, fraction_max 	  	O 	True 	Fraction (mole, mass, volume) maximum value for incompressible solutions
FRACTION_MIN, fraction_min 	  	O 	True 	Fraction (mole, mass, volume) minimum value for incompressible solutions
FUNDAMENTAL_DERIVATIVE_OF_GAS_DYNAMICS, fundamental_derivative_of_gas_dynamics 	  	O 	False 	Fundamental derivative of gas dynamics
GAS_CONSTANT, gas_constant 	J/mol/K 	O 	True 	Molar gas constant
GMOLAR, Gmolar 	J/mol 	O 	False 	Molar specific Gibbs energy
GWP100 	  	O 	True 	100-year global warming potential
GWP20 	  	O 	True 	20-year global warming potential
GWP500 	  	O 	True 	500-year global warming potential
G, GMASS, Gmass 	J/kg 	O 	False 	Mass specific Gibbs energy
HELMHOLTZMASS, Helmholtzmass 	J/kg 	O 	False 	Mass specific Helmholtz energy
HELMHOLTZMOLAR, Helmholtzmolar 	J/mol 	O 	False 	Molar specific Helmholtz energy
HH 	  	O 	True 	Health hazard
ISOBARIC_EXPANSION_COEFFICIENT, isobaric_expansion_coefficient 	1/K 	O 	False 	Isobaric expansion coefficient
ISOTHERMAL_COMPRESSIBILITY, isothermal_compressibility 	1/Pa 	O 	False 	Isothermal compressibility
I, SURFACE_TENSION, surface_tension 	N/m 	O 	False 	Surface tension
M, MOLARMASS, MOLAR_MASS, MOLEMASS, molar_mass, molarmass, molemass 	kg/mol 	O 	True 	Molar mass
ODP 	  	O 	True 	Ozone depletion potential
PCRIT, P_CRITICAL, Pcrit, p_critical, pcrit 	Pa 	O 	True 	Pressure at the critical point
PHASE, Phase 	  	O 	False 	Phase index as a float
PH 	  	O 	True 	Physical hazard
PIP 	  	O 	False 	Phase identification parameter
PMAX, P_MAX, P_max, pmax 	Pa 	O 	True 	Maximum pressure limit
PMIN, P_MIN, P_min, pmin 	Pa 	O 	True 	Minimum pressure limit
PRANDTL, Prandtl 	  	O 	False 	Prandtl number
PTRIPLE, P_TRIPLE, p_triple, ptriple 	Pa 	O 	True 	Pressure at the triple point (pure only)
P_REDUCING, p_reducing 	Pa 	O 	True 	Pressure at the reducing point
RHOCRIT, RHOMASS_CRITICAL, rhocrit, rhomass_critical 	kg/m^3 	O 	True 	Mass density at critical point
RHOMASS_REDUCING, rhomass_reducing 	kg/m^3 	O 	True 	Mass density at reducing point
RHOMOLAR_CRITICAL, rhomolar_critical 	mol/m^3 	O 	True 	Molar density at critical point
RHOMOLAR_REDUCING, rhomolar_reducing 	mol/m^3 	O 	True 	Molar density at reducing point
SMOLAR_RESIDUAL, Smolar_residual 	J/mol/K 	O 	False 	Residual molar entropy (sr/R = tau*dar_dtau-ar)
TCRIT, T_CRITICAL, T_critical, Tcrit 	K 	O 	True 	Temperature at the critical point
TMAX, T_MAX, T_max, Tmax 	K 	O 	True 	Maximum temperature limit
TMIN, T_MIN, T_min, Tmin 	K 	O 	True 	Minimum temperature limit
TTRIPLE, T_TRIPLE, T_triple, Ttriple 	K 	O 	True 	Temperature at the triple point
T_FREEZE, T_freeze 	K 	O 	True 	Freezing temperature for incompressible solutions
T_REDUCING, T_reducing 	K 	O 	True 	Temperature at the reducing point
V, VISCOSITY, viscosity 	Pa s 	O 	False 	Viscosity
Z 	  	O 	False 	Compressibility factor"""

def transformator(rawlistval):
	foo = [re.split('\s?\t\s?',l) for l in re.split('\n',rawlistval)]
	return foo

"""
>>> d = transformator(a)
>>> len(d)
73
>>> d[0]
['DELTA, Delta', '', 'IO', 'False', 'Reduced density (rho/rhoc)']
>>> d[-1]
['Z', '', 'O', 'False', 'Compressibility factor']
>>>
"""

def makeAliases(formteddata):
	foo = {}
	for fd in formteddata:
		foo[fd] = formteddata[0]
	return foo
"""
>>> makeAliases(d[2][0])
{' Dmass': 'D', ' DMASS': 'D', 'D': 'D'}
>>>
"""

class TIFPoint:
		"""
Thermodynamics of Incompressible Fluids:
Class TIFPoint calculated
TIFPoint based function PropsSI in module CoolProp.CoolProp.
	"""
	def __init__(self, P=101325, **kwargs):

		assert len(kwargs)<3, "слишком много параметров на входе"

		self._in = []
		[self._in.extend([k,v]) for k, v in kwargs.items()]

		self.P = P
		for key, val in kwargs.items():
			setattr(self, key, val)

	def _map(self, attr):
		_aliases = {
			"T":"Tdb",
			"B": "Twb",
			"D": "Tdp",
			"V": "Vda",
			"R": "RH",
			"W": "Omega",
			"H": "Hda",
			"S": "Sda",
			"C": "cp",
			"M": "Visc"}
		try:
			return  _aliases[attr]
		except KeyError:
			return attr

	def __getattr__(self, attrname):
		_names = (  "T", "Tdb",
			    "B", "Twb",
			    "D", "Tdp",
			    "P",
			    "V", "Vda", "Vha",
			    "R", "RH",
			    "W", "Omega",
			    "H", "Hda", "Hha",
			    "S", "Sda", "Sha",
			    "C", "cp", "Cha",
			    "M", "Visc",
			    "K")

		attr = self._map(attrname)

#		print("get attr name: %s" % attrname)

		if attr in _names:
			val = self.__dict__[attr] = HAPropsSI(attr,"P", self.P, *self._in)
#			print("RETURN attr name: %s" % attr)
			return val
		else:
			raise TypeError('unknown attr:' + attrname)
		#ject.__getattr__(self, attrname)

	@cached_property
	def rho(self):
		return 1/self.V

	def __str__(self):
		return "вызов метода STR"

def main():

	return 0

if __name__ == "__main__":
  import doctest
  doctest.testmod()
