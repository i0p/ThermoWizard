class wather(iapws.IAPWS97):
""" наследует класс
умеет складывать водЫ
>>> w1 = wather(t=22)
>>> w2 = wather(t=90)
>>> w = w1 + w2
>>> w.t
56.0
>>> w2 = wather(t=90,m = 15)
>>> w = w1 + w2
"""
	def __init__(self, t = 20, B = 101325,m = 1):
		super().__init__(T = 273.16 + t, P = B * 1e-6)
		self.t = t
		self.B = B
		self.m = m
	@property
	def t(self):
		return self.__t
	@t.setter
	def t(self,t):
		super().__init__(T = 273.16 + t, P = self.P)
		self.__t = t
	@property
	def B(self):
		return self.__B
	@B.setter
	def B(self,B):
		super().__init__(T = self.T, P = B*1e-6)
		self.__B = B
	def __add__(self,other):
		t = (self.t*self.m + other.t*other.m) / (self.m + other.m)
		return wather(t = t)
	def __repr__(self):
		return "\
    P       = {0.P:>17.15f} - Pressure, MPa \
    T       = {0.T:>17.15f} - Temperature, K \
    g       = {0.g:>17.15f} - Specific Gibbs free energy, kJ/kg \
    a       = {0.a:>17.15f} - Specific Helmholtz free energy, kJ/kg \
    v       = {0.v:>17.15f} - Specific volume, m³/kg \
    rho     = {0.rho:>17.15f} - Density, kg/m³ \
    h       = {0.h:>17.15f} - Specific enthalpy, kJ/kg \
    u       = {0.u:>17.15f} - Specific internal energy, kJ/kg \
    s       = {0.s:>17.15f} - Specific entropy, kJ/kg·K \
    cp      = {0.cp:>17.15f} - Specific isobaric heat capacity, kJ/kg·K \
    cv      = {0.cv:>17.15f} - Specific isochoric heat capacity, kJ/kg·K \
    Z       = {0.Z:>17.15f} - Compression factor \
    gamma   = {0.gamma:>17.15f} - Isoentropic exponent \
    alfav   = {0.alfav:>17.15f} - Isobaric cubic expansion coefficient, 1/K \
    kt      = {0.kt:>17.15f} - Isothermal compressibility, 1/MPa \
    alfap   = {0.alfap:>17.15f} - Relative pressure coefficient, 1/K \
    betap   = {0.betap:>17.15f} - Isothermal stress coefficient, kg/m³ \
    joule   = {0.joule:>17.15f} - Joule-Thomson coefficient, K/MPa \
    deltat  = {0.deltat:>17.15f} - Isothermal throttling coefficient, kJ/kg·MPa \
    region  = {0.region:>17} - Region \
    w       = {0.w:>17.15f} - Speed of sound, m/s \
    mu      = {0.mu:>17.15f} - Dynamic viscosity, Pa·s \
    nu      = {0.nu:>17.15f} - Kinematic viscosity, m²/s \
    k       = {0.k:>17.15f} - Thermal conductivity, W/m·K \
    alfa    = {0.alfa:>17.15f} - Thermal diffusivity, m²/s \
    sigma   = {0.sigma:>17.15f} - Surface tension, N/m \
    epsilon = {0.epsilon:>17.15f} - Dielectric constant \
    n       = {0.n:>17.15f} - Refractive index \
    Pr      = {0.Pr:>17.15f} - Prandtl number".format(self)
