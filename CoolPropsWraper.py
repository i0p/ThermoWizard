from CoolProp.CoolProp import PropsSI
from tabulate import tabulate
class mainProps:
	props = {
                "t": ("Temperature", "C"),
		"T": ("Temperature", "K"),
		"D": ("Mass density", "kg/m^3"),
		"Cpmass":("Specific heat", "J/kg/K"),
		"L": ("Termal conductivity", "W/m/K"),
		"V": ("Viscosity", "Pa s"),
		"PRANDTL": ("Prandtl number", ""),
                "T_freeze": ("Freezing temperature for incompressible solutions", "K")
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

def capacity(t1, t2, mflow=None, vflow=None, media="Water", P=101325):
	T = lambda t: 273.15+t
	H1 = PropsSI("H", "P", P, "T", T(t1), media)
	D1 = PropsSI("D", "P", P, "T", T(t1), media)
	H2 = PropsSI("H", "P", P, "T", T(t2), media)
	D2 = PropsSI("D", "P", P, "T", T(t2), media)
	flow1 = mflow or vflow*D1
	flow2 = mflow or vflow*D2
	return (H2-H1)*flow1, (H2-H1)*flow2

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
			s = "{t:4.1f}\t{T:5.2f}\t{L:.4f}\t{PRANDTL:.1f}\t{D:.1f}\t{V:.2e}\t{Cpmass:.1f}".format(
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
       "ZMC" : "Zitrec MC, Ethylene Glycol"}

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

