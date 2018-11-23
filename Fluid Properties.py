#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Fluid Properties.py
#
#  @Copyright: 2018 by boober <looking.at.buildings@gmail.com>
#
#  @license: GNU GPL, see COPYING for details.

### выводит теплофизические свойства водных растворов, в частности этиленгликолей и пропилен гликолей
from CoolProp.CoolProp import PropsSI

map_ = {"T": "Температура, °C", "D": "Плотность, кг/м**3",
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
	T_k = lambda cels: T0+cels
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
		foo = [str(t(T))]
		for prop in props:
			foo.append(
				"{:.7f}".format(
					PropsSI(
						prop, "T", T, "P", P, incomp
						)
					)
				)

		return "\t".join(foo)
	print_header(props)
	print(strOut(round(T_freeze+3e-4,4)))
	t_start = t_ = int(ABS(t((T_freeze))))
	t_stop = 110
	step = 2.5 # шаг температуры
	while t_<= t_stop:
		try:
			print(strOut(T_k(t_)))
		except ValueError:
			pass
		t_ += step

"""
>>> O("MEG-40%")
Температура, °C	Плотность, кг/м**3	Теплоемкость, Ср, кДж/(кг*К)	Теплопроводность, Вт/(м*К)	Динамическая вязкость, [Па*с]
-23.812599999999975	1067.5963430	3326.5888828	0.3915737	0.0185098
-20.0	1066.6730663	3344.2501968	0.3944972	0.0150007
-15.0	1065.3251977	3367.1753812	0.3983399	0.0115576
-10.0	1063.8254763	3389.8195451	0.4021901	0.0090507
-5.0	1062.1778752	3412.1690531	0.4060450	0.0071985
0.0	1060.3863670	3434.2102700	0.4099019	0.0058107
5.0	1058.4549247	3455.9295605	0.4137581	0.0047569
10.0	1056.3875211	3477.3132894	0.4176108	0.0039465
15.0	1054.1881291	3498.3478214	0.4214574	0.0033158
20.0	1051.8607216	3519.0195211	0.4252951	0.0028191
25.0	1049.4092714	3539.3147533	0.4291211	0.0024238
30.0	1046.8377514	3559.2198828	0.4329328	0.0021057
35.0	1044.1501345	3578.7212742	0.4367273	0.0018472
40.0	1041.3503934	3597.8052923	0.4405021	0.0016351
45.0	1038.4425012	3616.4583018	0.4442544	0.0014593
50.0	1035.4304306	3634.6666675	0.4479813	0.0013122
55.0	1032.3181545	3652.4167540	0.4516803	0.0011880
60.0	1029.1096457	3669.6949260	0.4553486	0.0010821
65.0	1025.8088772	3686.4875483	0.4589834	0.0009909
70.0	1022.4198218	3702.7809857	0.4625820	0.0009116
75.0	1018.9464524	3718.5616028	0.4661417	0.0008419
80.0	1015.3927418	3733.8157643	0.4696598	0.0007800
85.0	1011.7626628	3748.5298350	0.4731336	0.0007243
90.0	1008.0601884	3762.6901796	0.4765602	0.0006738
95.0	1004.2892915	3776.2831629	0.4799371	0.0006275
100.0	1000.4539448	3789.2951495	0.4832614	0.0005844
"""

def main(foo):

	return 0

if __name__ == "__main__":
        import sys
        sys.exit(main(sys.argv))
