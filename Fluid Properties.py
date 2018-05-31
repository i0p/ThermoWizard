#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Fluid Properties.py
#
#  @Copyright: 2018 by boober <looking.at.buildings@gmail.com>
#
#  @license: GNU GPL, see COPYING for details.

### выводит теплофизические свойства водных растворов, в частности этиленгликолей и пропилен гликолей

map_ = {"T": "Температура, K", "D": "Плотность, кг/м**3",
	"Cvmass": "Теплоемкость, Ср, кДж/(кг*К)",
	"CONDUCTIVITY":"Теплопроводность, Вт/(м*К)",
	"VISCOSITY":"Динамическая вязкость, [Па*с]"}

def ABS(n):
	""""""
	m = 1 if n > 0 else -1
	foo = abs(n)//10*10
	return m*foo

def O(fluid='MEG-36%'):
	props = ["D", "Cvmass", "CONDUCTIVITY", "VISCOSITY"]
	T0=273.15
	t = lambda K: K-T0
	incomp="INCOMP::%s" % fluid
	P=101325
	T_freeze = PropsSI("T_freeze", "T", T0, "P", P, incomp)
	def print_header(props):
		#nonlocal map_
		h = [map_["T"]]
		for prop in props:
			h.append(map_[prop])
		print("\t".join(h))

	def strOut(T):
		nonlocal props
		nonlocal incomp
		nonlocal P
		foo = [str(T)]
		for prop in props:
			foo.append(
				"{:.4f}".format(
					PropsSI(
						prop, "T", T, "P", P, incomp
						)
					)
				)

		return "\t".join(foo)
	print_header(props)
	print(strOut(round(T_freeze+3e-4,4)))
	T_start=int((ABS(T_freeze)))
	T_stop = T_start+110
	for T in range(T_start, T_stop, 10):
		try:
			print(strOut(T))
		except ValueError:
			pass

"""
>>> O("MPG-35%")
Температура, K	Плотность, кг/м**3	Теплоемкость, Ср, кДж/(кг*К)	Теплопроводность, Вт/(м*К)	Динамическая вязкость, [Па*с]
256.8298	1042.2869	3676.3929	0.3969	0.0253
260	1041.4568	3686.0550	0.3990	0.0204
270	1038.2945	3716.3933	0.4057	0.0110
280	1034.3663	3746.4982	0.4126	0.0065
290	1029.7499	3776.3414	0.4197	0.0041
300	1024.5231	3805.8949	0.4268	0.0028
310	1018.7635	3835.1306	0.4341	0.0020
320	1012.5490	3864.0205	0.4414	0.0015
330	1005.9572	3892.5364	0.4487	0.0012
340	999.0658	3920.6503	0.4561	0.0010
350	991.9527	3948.3342	0.4633	0.0008
"""

def main():

	return 0

if __name__ == "__main__": sys.exit(main(sys.argv))
