import math
from CoolProp.HumidAirProp import HAPropsSI

T  = lambda t: 273.15+t
t  = lambda T: T-273.15
P0 = 101325
B  = 99e3

P = lambda h: P0*10**(-0.06*(h/1000)) #

def P_(h, t):	
	M=0.029
	g=9.81
	R=8.31
	return P0*math.e**(-1*M*g*h/(R*T(t)))
    
def airHeating(t1, t2, R1=None, H1=None, B=99000):
	#assert (R1 is not None and H1 is not None), "ERROR"
	H1 = H1 or HAPropsSI('Hha','T',T(t1),'P',B,'R',R1)
	W1 = HAPropsSI('W','T',T(t1),'P',B,'Hha',H1)
	Vh1 = HAPropsSI('Vha','T',T(t1),'P',B,'Hha',H1)
	V1 = HAPropsSI('V','T',T(t1),'P',B,'Hha',H1)
	H2 = HAPropsSI('Hha','T',T(t2),'P',B,'W',W1)
	Vh2 = HAPropsSI('Vha','T',T(t2),'P',B,'Hha',H2)
	V2 = HAPropsSI('V','T',T(t2),'P',B,'Hha',H2)
	return (H1, H2, 1/V1, 1/V2, 1/Vh1, 1/Vh2)

""">>> L=286650
>>> foo = airHeating(35, 44.4, R1=0.23)
>>> g=L/3600*foo[-1]
>>> g*(foo[1]-foo[0])
820410.2859891736
"""
