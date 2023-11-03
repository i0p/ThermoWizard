from CoolProp.CoolProp import PropsSI, HAPropsSI
from tabulate import tabulate
import re

class mainProps:
	props = {
		"t": ("Temperature", "C"),
		"T": ("Temperature", "K"),
		"D": ("Mass density", "kg/m^3"),
		"Cpmass":("Specific heat", "J/kg/K"),
		"L": ("Termal conductivity", "W/m/K"),
		"V": ("Viscosity", "Pa s"),                
		"PRANDTL": ("Prandtl number", ""),
		#"T_freeze": ("Freezing temperature for incompressible solutions", "K")
		}
	def __init__(self, T=273.15, P=101325,medianame="Water"):
		self.T = T
		self.P = P
		self.medianame = medianame
		
	def t(self):
		return self.T - 273.15
	
	def mainProps(self):
		foo = {}
		foo["t"] = self.t()
		for prop in self.props:
			try:
				foo[prop] = PropsSI(prop, "P", self.P, "T", self.T, self.medianame)
			except ValueError as err:
				if "Output parameter parsing failed; error:" in err.args[0]: pass
				else:
					raise ValueError(err.args)
		return foo
	
	def pprint(self):
		foo = []
		mprops = self.mainProps()
		formatstring = "{:23} {:7} {:8.4f}"
		for prop in self.props:
			foo.append(formatstring.format(self.props[prop][0],self.props[prop][1], mprops[prop]))
		print("\n".join(foo))
	def pprintt(self):
		foo = []
		mprops = self.mainProps()
		formatstring = "{}\t{}\t{}"
		for prop in self.props:
			foo.append(formatstring.format(self.props[prop][0],self.props[prop][1], mprops[prop]))
		print("\n".join(foo))

		
""">>> for t in range(5,16):
	mainProps(T=273.15+t,medianame="INCOMP::APG-40%").pprintt()
	print()

	
>>> for t in range(40,51):
	mainProps(T=273.15+t,medianame="INCOMP::APG-40%").pprintt()
	print()

>>> for t in range(-25,0,1):
	mp = mainProps(T=273.15+t/10,medianame="INCOMP::APG-40%").mainProps()
	s = "{t}\t{T}\t{L}\t{PRANDTL}\t{D}\t{V}\t{Cpmass}".format(
		t=mp["T"]-273.15,
		T=mp["T"],
		L=mp["L"],
		PRANDTL=mp["PRANDTL"],
		D=mp["D"],
		V=mp["V"],
		Cpmass=mp["Cpmass"])
	print(s.replace(".", ","))"""

class ThermoWizard:
    def __init__(self, T=273.15, P=101325, medianame="Water"):
        self.T = T
        self.P = P
        self.medianame = medianame

    def temperature_in_celsius(self): return self.T - 273.15
    
    def calculate_properties(self):
        props = {}
        props["t"] = self.temperature_in_celsius()
        for prop, (name, unit) in self.get_property_map().items():
            if prop == "T_freeze":
                try:
                    props[prop] = PropsSI(prop, "P", self.P, "T", self.T, self.medianame)
                except ValueError as err:
                    if "calc_T_freeze is not implemented" in err.args[0]:
                        props[prop] = "N/A"
            else:
                try:
                    props[prop] = PropsSI(prop, "P", self.P, "T", self.T, self.medianame)
                except ValueError as err:
                    if "Output parameter parsing failed; error:" not in err.args[0]:
                        raise ValueError(err.args)
        return props

    def get_property_map(self):
        property_map = {
            "t": ("Temperature", "C"),
            "T": ("Temperature", "K"),
            "D": ("Mass density", "kg/m^3"),
            "Cpmass": ("Specific heat", "J/kg/K"),
            "L": ("Termal conductivity", "W/m/K"),
            "V": ("Viscosity", "Pa s"),
            "PRANDTL": ("Prandtl number", ""),
        }
        try:
            PropsSI("T_freeze", "P", self.P, "T", self.T, self.medianame)
            property_map["T_freeze"] = ("Freezing temperature", "K")
        except ValueError as err:
            if "calc_T_freeze is not implemented" in err.args[0]:
                property_map["T_freeze"] = ("Freezing temperature", "N/A")
        return property_map

    def pretty_print(self, units="SI"):
        props = self.calculate_properties()
        formatstring = "{}\t{}\t{}" if units == "SI" else "{}\t{}"
        result = [formatstring.format(name, unit, props.get(prop, "N/A")) for prop, (name, unit) in self.get_property_map().items()]
        print("\n".join(result))

"""
# Пример использования класса
>>> tw = ThermoWizard(T=300, P=100000, medianame="Water")
>>> tw.pretty_print(units="SI")
"""
###
### класс ThermoWizard замена mainprops
###

def capacity(t1, t2, mflow=None, vflow=None, media="Water", P=101325):
	T = lambda t: 273.15+t
	H1 = PropsSI("H", "P", P, "T", T(t1), media)
	D1 = PropsSI("D", "P", P, "T", T(t1), media)
	H2 = PropsSI("H", "P", P, "T", T(t2), media)
	D2 = PropsSI("D", "P", P, "T", T(t2), media)
	flow1 = mflow or vflow*D1
	flow2 = mflow or vflow*D2
	return (H2-H1)*flow1, (H2-H1)*flow2

def FlowWaterHeatingPower(t1, t2, capacity, media="Water", P=101325):
	T = lambda t: 273.15+t
	H1 = PropsSI("H", "P", P, "T", T(t1), media)
	D1 = PropsSI("D", "P", P, "T", T(t1), media)
	H2 = PropsSI("H", "P", P, "T", T(t2), media)
	D2 = PropsSI("D", "P", P, "T", T(t2), media)
	mflow = capacity/(H2-H1)
	
	return mflow, mflow/D1, mflow/D2 # kg/s, m3/s, m3/s

def DisplayFluidValues(fluid,temp=[],concentration=40):
	print("Fluid name: %s" % MEDIA[fluid])
	print("Fluid desc: %s-%d%%" % (fluid, concentration))
	tf = mainProps(T=273.15,medianame="INCOMP::%s-%d%%" % (fluid, concentration)).mainProps()
	print("{}: {:.1f}C".format(mainProps.props["T_freeze"][0], tf["T_freeze"]-273.15))
	tab=[]
	seq=["t", "T", "L", "PRANDTL", "D", "V", "Cpmass"]
	for t in temp:
		try:
			mp = mainProps(T=273.15+t,medianame="INCOMP::%s-%d%%" % (fluid, concentration)).mainProps()
			s = "{t:4.1f}\t{T:5.2f}\t{L:.4f}\t{PRANDTL:.1f}\t{D:.1f}\t{V:.2e}\{Cpmass:.1f}".format(
				t=mp["T"]-273.15,
				T=mp["T"],
				L=mp["L"],
				PRANDTL=mp["PRANDTL"],
				D=mp["D"],
				V=mp["V"],                             
				Cpmass=mp["Cpmass"])
			tab.append( [ mp[prop] for prop in seq] )
			#print(s.replace(".", ","))
			#print(s)
		except ValueError : pass
	print(tabulate(tab, headers=[ ", ".join(mainProps.props[key]) for key in seq]))
"""
>>> DisplayFluidValues("MEG", [-26, -16, -6, 4, 14,24,34,44], concentration=43)
"""

"""
>>> capacity(-2.5, 10, 79.1/3600, media="INCOMP::MPG-40%")
(1047070.184762935, 1041235.7752152518)
>>> capacity(-2.5, 10, 79.1/3600, media="INCOMP::APG-40%")
(1048072.2911979043, 1042912.6186197766)
>>> for tout in 6.6, 4.8, 3.8, 3.1, 1.4, -0.4, -2.5:
	print("{:4.1f}: {:9.1f} kW / {:9.1f} kW".format(tout,*capacity(tout, 10, 79.1/3600, media="INCOMP::APG-40%")))
"""

MEDIA={"MEG": "Ethylene Glycol - aq",
       "MEG2": "Melinder, Ethylene Glycol",
       "AEG" : "ASHRAE, Ethylene Glycol",
       "AN"  : "Antifrogen N, Ethylene Glycol",
       "GKN" : "Glykosol N, Ethylene Glycol",
       "ZM"  : "Zitrec M, Ethylene Glycol",
       "ZMC" : "Zitrec MC, Ethylene Glycol",
       "AL"  : "Antifrogen L, Propylene Glycol",
       "APG" : "ASHRAE, Propylene Glycol",
       "PKL" : "Pekasol L, Propylene Glycol",
       "ZFC" : "Zitrec FC, Propylene Glycol",
       "ZLC" : "Zitrec LC, Propylene Glycol",
       "Water": "Fresh water IAPWS 97"}

"""
>>> for media in MEDIA:
	try:
		Q1,Q2 = capacity(40,50,vflow=45.19/1000, media="INCOMP::%s-40%%" % media )
		print("{:4} : {:9.1f}...{:9.1f}".format(media, Q1,Q2))
	except ValueError:
		print("Error media '%s - %s'" % (media, MEDIA[media]))
"""
"""
>>> for media in MEDIA:
	try:
		Q1,Q2 = capacity(40,50,vflow=43.12/1000, media="INCOMP::%s-40%%" % media)
		print("{:29} {:^3}: {:6.2f} / {:6.2f} kW".format(MEDIA[media], media, Q1*1e-3, Q2*1e-3))
	except ValueError: pass
"""

class humidairprops:
	def __init__ (self, t, R=None, W=None, Hha=None, P=99700):
		self.t, self.P = t, P
		if R is not None:
			self.R = R
			self.W = HAPropsSI('W','T',self.T,'P',self.P,'R',self.R)	# Humidity Ratio [kg water/kg dry air]
			self.Hha = HAPropsSI('Hha','T',self.T,'P',self.P,'R',self.R)
		elif W is not None:
			self.W = W
			self.R = HAPropsSI('R','T',self.T,'P',self.P,'W',self.W)
			self.Hha = HAPropsSI('Hha','T',self.T,'P',self.P,'W',self.W)
		elif Hha is not None:
			self.Hha = Hha                                                  # Mixture enthalpy per humid air[J/kg humid air]
			self.R = HAPropsSI('R','T',self.T,'P',self.P,'Hha',self.Hha)
			self.W = HAPropsSI('W','T',self.T,'P',self.P,'Hha',self.Hha)
		
		self.Vha = HAPropsSI('Vha','T',self.T,'P',self.P,'R',self.R)	# Mixture volume per unit humid air
		self.Vda = HAPropsSI('Vda','T',self.T,'P',self.P,'R',self.R)	# Mixture volume per unit dry air
		self.h = HAPropsSI('H','T',self.T,'P',self.P,'R',self.R)	# Mixture enthalpy per dry air
		self.cp = HAPropsSI('C','T',self.T,'P',self.P,'R',self.R)	# Mixture specific heat per unit dry air
		self.Cha = HAPropsSI('Cha','T',self.T,'P',self.P,'R',self.R)	# Mixture specific heat per unit humid air
		self.Twb = HAPropsSI('Twb','T',self.T,'P',self.P,'R',self.R)	# Wet-Bulb Temperature
		self.Tdp = HAPropsSI('Tdp','T',self.T,'P',self.P,'R',self.R)	# Dew-Point Temperature
		self.K = HAPropsSI('Tdp','T',self.T,'P',self.P,'R',self.R)	# Mixture thermal conductivity [W/m/K]
		self.mu = HAPropsSI('mu','T',self.T,'P',self.P,'R',self.R)	# Mixture viscosity [Pa-s]		
		
	@property
	def T(self):
		return self.t + 273.15
	@property
	def rho(self):		
		return 1/self.Vha

class Capacity:
	UNITS={"m3/h": 1/3600,
	       "m3/s" : 1
	       }
	def __init__ (self, p1, p2, flow, units= "m3/h"):
		self.p1, self.p2, self.flow, self.units = p1, p2, flow, units
	@property
	def multi(self):
		return self.UNITS[self.units]

	def Total(self, t2=None):
		p2 = self.p2
		if t2:			
			p2 = self._p2 = humidairprops(t2,
						      R=HAPropsSI('R','T', t2+273.15,'P', p1.P,'W',p1.W)
						      )					#тут будет дополнительная точка
		return self.flow * self.multi*self.p1.Vha*(p2.h-self.p1.h)

	def Sensible(self, t2=None):
		p2 = self.p2
		if t2:
			self.Total(t2)
			p2 = self._p2

		return self.flow * self.multi * self.p1.cp * self.p1.Vha * (p2.t - self.p1.t)

"""
>>> p1 = humidairprops(18,R=0.5, P=101325)
>>> p2 = humidairprops(
	24,
	R=HAPropsSI('R','T', 24+273.15,'P', p1.P,'W',p1.W)
	)
>>> cpct = Capacity(p1, p2, flow=1690)
>>> cpct.Total()
3465.3091078225675
>>> cpct.Sensible()
3465.0050922393866
"""

def Cooling(p1, t2):
	try:
		p2 = humidairprops(t2,
			      W=HAPropsSI('W','T', t2+273.15,'P', p1.P,'W',p1.W)
			      )
	except:                                       #исключение вообще никак не обоработано
		p2 = humidairprops(t2, R=0.99)
	return p2

""">>> p2 = Cooling(p1, 13)"""


###----------расчет многих расходов


"""
>>> rawInput='''21600	21600	26,3/13,0	26,3/13,2
34900	39672	32,0/13,0	26,3/13,2
20300	22968	32,0/13,0	26,3/13,2
36100	22968	32,0/13,0	26,3/13,2
38170	37332	32,0/13,0	26,3/13,2
13600	9972 	22,0/11,0	26,3/13,2
15000	22968	22,0/11,0	26,3/13,2
15000	22968	22,0/11,0	26,3/13,2
15000	9972	22,0/11,0	26,3/13,2
16000	22968	22,0/11,0	26,3/13,2
12000	0	24,5/19,5	0'''
"""

I = 56800 #J/kg humid air
indexmap= ((0,2,3), (1,4,5))

def transform(raw):
	pat = re.compile("[,]")
	pat2 = re.compile(r"\s?/\s?")
	sep = [	[float(n) for n in line.split() ] for line in pat2.sub( "\t", pat.sub(".",raw)).split("\n")]
	return sep

def massCalc(rawInput):
	Total = []
	for paramset in transform(rawInput):
		foo = []
		for indx in indexmap:
			flow = paramset[indx[0]]
			t1 = paramset[indx[1]]
			t2 = paramset[indx[2]]
			try:
				p1 = humidairprops(t1,
					   Hha=I,
					    P=99100
					   )
			except:                                       #исключение вообще никак не обоработано
				p1 = humidairprops(t1,
					   R=0.56,
					    P=99100
					   )
			p2 = Cooling(p1, t2)
			foo.append( Capacity(p2,p1,flow).Total() )
		Total.append(foo)
	return Total

def ppRint(foo):
	for line in foo:
		print(f"{line[0]/1000:.1f}\t{line[1]/1000:.1f}")

"""
>>> Tot = massCalc(rawInput2)
>>> ppRint(Tot)
102.4	99.9
164.4	183.5
95.6	106.2
170.1	106.2
179.8	172.7
79.9	46.1
88.1	106.2
88.1	106.2
88.1	46.1
94.0	106.2
14.6	0.0"""

'''>>> rawInput0="""14000	14000	28,5/13,0	0/0
14000	14000	28,5/13,0	0/0
20000	20000	28,5/12,0	0/0
30000	30000	28,5/13,0	0/0"""
>>> ppRint(
	massCalc(rawInput0)
	)
66.2	0.0
66.2	0.0
105.9	0.0
141.9	0.0'''

class pipe:
	pipepattern = re.compile(r"(?P<Dout>\d+([,.]\d+)?)[xх](?P<thin>\d+([,.]\d+)?)", re.I)
	def __init__(self, size):
		self.size = size
		self.parse()
	def parse(self):
		s = self.pipepattern.search(
			re.sub("[,.]",".",
			       self.size)
			)
		self.Dout = float(s.group("Dout"))
		self.thin = float(s.group("thin"))
		return True
	@property
	def Din(self):
		return self.Dout - self.thin*2
	@property
	def UV1(self):
		return f"{self.Dout:g}x{self.thin:.1f}"
	def __str__(self):
		return f"{self.Din:g} {self.Dout:g} {self.UV1}"

def heating(t1, R1, t2, flow, P=101235, units="m3/h"):
	p1 = humidairprops(t=t1, R=R1, P=P)

	cpct = Capacity(p1=p1,
			p2=humidairprops(t=t2,
					R=HAPropsSI('R','T', t2+273.15,'P', P,'W',p1.W),
					P=P),
			flow=flow,
			units=units
			)
	return cpct

"""
>>> foo = heating(18, 0.50, 24, 930)
>>> foo.Total()
1905.261631254459
>>> foo.Sensible()
1905.0944160104882
"""

T = lambda t: 273.15+t

for t, R in ((-15, 0.85), (0,0.85), (8,0.6), (26,0.526)):
	p1 = humidairprops(
		t=t, R=R,
		P=101325)
	p2 = humidairprops(
		t=20,
		R=HAPropsSI('R','T', T(20),'P', p1.P,'W',p1.W)
		)
	p3 = humidairprops(
		t=25,
		R=HAPropsSI('R','T', T(25),'P', p1.P,'W',p1.W)
		)
	print(f"{p1.t} ->\t{p2.t}°C\t{p2.R*100:2.1f}%\n\t{p3.t}°C\t{p3.R*100:2.1f}%")

###=== KVS

def DP(Q, Kvs, rho):
	"""Kv = m3/h - Flow coefficient
Q = m3/h - Flow
Qn = m3n/h - Normal flow (20°C 760mm Hg)
P1 = bar - Inlet pressure - (Gauge pressure + 1)
P2 = bar - Outlet pressure - (Gauge pressure – 1)
DP = bar - Pressure drop - (Differential pressure between inlet and outlet pressure)
r = Kg/dm³ - Relative density with respect to water (Water at 4°C = 1)
rn = Kg/dm³ - Normal relative density as to the air
G = Kg/h - Mass
t = °C - Inlet media temperature
V1 = m3/Kg - Inlet specific volume
V2 = m3/Kg - Outlet specific volume referred to “P2” pressure and “t” temperature"""
	return rho * (Q/Kvs)**2

""">>> DP(Q=13.1,
   Kvs=83,
   rho=PropsSI('D', 'T', 273.15+5, 'P', 101325, 'INCOMP::AN-45%')/1000
   )*1e5
2692.6515791546803"""	
