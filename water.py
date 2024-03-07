from iapws import IAPWS97
class water(IAPWS97):
        """
        умеет складывать водЫ
        """
        def __init__(self, t=20, B=101325, m=1):
                """Constructor"""
                super().__init__(T=273.16+t, P=B*1e-6)
                self.t = t
                self.B = B
                self.m = m
        @property
        def t(self):
                return self.__t
        @t.setter
        def t(self,t):
                super().__init__(T=273.16+t, P=self.P)
                self.__t = t
        @property
        def B(self):
                return self.__B
        @B.setter
        def B(self,B):
                super().__init__(T=self.T, P=B*1e-6)
                self.__B = B
        def __add__(self,other):
                mm = self.m + other.m
                T = (self.cp*self.T*self.m + other.cp*other.T*other.m) / ( self.cp*self.m + other.cp*other.m)
                return water(t=T-273.16, m=mm, B=self.B)

def tostring(element_IAPWS97):
        """    Serialize an element to an encoded string representation of its IAPWS97. """
        d = {'P':('Pressure','MPa'),
                'T':('Temperature','K'),
                't':('Temperature','C'),
                'g':('Specific Gibbs free energy','kJ/kg'),
                'a':('Specific Helmholtz free energy','kJ/kg'),
                'v':('Specific volume','m³/kg'),
                'rho ':('Density','kg/m³'),
                'h':('Specific enthalpy','kJ/kg'),
                'u':('Specific internal energy','kJ/kg'),
                's':('Specific entropy','kJ/kg·K'),
                'cp':('Specific isobaric heat capacity','kJ/kg·K'),
                'cv':('Specific isochoric heat capacity','kJ/kg·K'),
                'Z':('Compression factor',''),
                'f':('Fugacity','MPa'),
                'gamma':('Isoentropic exponent',''),
                'alfav':('Isobaric cubic expansion coefficient','1/K'),
                'kt':('Isothermal compressibility','1/MPa'),
                'alfap':('Relative pressure coefficient','1/K'),
                'betap':('Isothermal stress coefficient','kg/m³'),
                'joule ':('Joule-Thomson coefficient','K/MPa'),
                'deltat':('Isothermal throttling coefficient','kJ/kg·MPa'),
                'region  ':('Region',''),
                'w':('Speed of sound','m/s'),
                'mu':('Dynamic viscosity','Pa·s'),
                'nu':('Kinematic viscosity','m²/s'),
                'k':('Thermal conductivity','W/m·K'),
                'alfa':('Thermal diffusivity','m²/s'),
                'sigma':('Surface tension','N/m'),
                'epsilon ':('Dielectric constant',''),
                'n':('Refractive index',''),
                'Pr':('Prandtl number',''),
                'Prandt':('Prandtl No','')
             }
        s = []
        s.append('Properties:')
        for key in d:
                value = element_IAPWS97.__dict__.get(key)       
                if value is not None:
                        prop = d.get(key)
                        try:
                                s.append("{discription:37}:{parm:^8}:{val:>11.4g} {unit:<11}".format(parm=key, val=value, unit=prop[1], discription=prop[0]))
                        except TypeError:
                                print(key, element_IAPWS97.__dict__[key])
        return "\n".join(s)

class heat2flow(object):
        """
        возвращает расход теплоносителя, kg/m³/s
        Q - мощность тепловая, Вт
        t1, t2 - температура, C
        """
        def __init__(self, **data):
                """constructor [невыдерживает никакой критики...., переписать]
                необходимо исключить возможность указания одинаковых по смыслу значений, как-то нельзя одновременно использовать Q и flow, ибо они вычисляются одно из другого"""
                self.t_in = data.get("t1")
                self.t_out = data.get("t2")
                self.Q = data.get("Q")
                self.flow = data.get("flow")
        @property
        def flow(self):
                return self.__flow
        @flow.setter
        def flow(self, flow):
                if flow is not None:
                        self.__flow = flow
                        self.__Q = flow*(self.__w1.h - self.__w2.h)*1e3
        @property
        def Q(self):
                return self.__Q
        @Q.setter
        def Q(self, Q):
                if Q is not None:
                        self.__Q = Q
                        self.__flow = (Q/(self.__w1.h - self.__w2.h))*1e-3
        @property
        def t_in(self):
                return self.__t1
        @t_in.setter
        def t_in(self, t_in):
                if t_in is not None:
                        self.__w1 = water(t_in)
                        self.__t1 = t_in
        @property
        def t_out(self):
                return self.__t2
        @t_out.setter
        def t_out(self, t_out):
                self.__w2 = water(t_out)
                self.__t2 = t_out
        def __str__(self):
                def altFlow(flow, w):
                        vf_l = flow/w.rho*1e3
                        vf_m = flow*w.v*3.6e3
                        vf_h = vf_l * 3600              # часовой расход
                        param = "t={0}°C".format(w.t)
                        s = "{parm:>15}:{val:>8.4f} {unit:<6} {val_h:>8.4f} l/h    {alt_val:>6.4f} {alt_unit:<4} ".format(
                                                                                parm=param, unit="l/s", val=vf_l, val_h=vf_h, alt_val=vf_m, alt_unit='m³/h')
                        return s

                s = []
                s.append("{parm:<15}:{val:>8.1f} {unit:<6}".format(parm="Duty", unit="W", val=self.Q))
                s.append("{parm:<15}:{val:>8} {unit:<6}".format(parm="Fluid", unit="100%", val="Water"))
                s.append("{parm:<15}:{val:>8.1f} {unit:<6}".format(parm="Fluid on", unit="°C", val=self.t_in))
                s.append("{parm:<15}:{val:>8.1f} {unit:<6}".format(parm="Fluid on", unit="°C", val=self.t_out))
                s.append("{parm:<15}:{val:>8.3f} {unit:<6}".format(
                                                                                parm="Fluid flow rate", unit="kg/s", val=self.flow))
                s.append("{0:<15}:".format("Volume flow"))                                                      
                s.append(altFlow(self.flow, self.__w1))
                s.append(altFlow(self.flow, self.__w2))
                return "\n".join(s)

def table_I6():
        point = (water.water(t=t) for t in range(0,200,10))
        for w in point:
                print("{w.t}\t{w.rho:^5.4g}\t{w.h:^5.4g}\t{w.cp:^5.4g}\t{w.k:^5.4g}\t{w.alfa:^5.4g}\t{w.mu:^5.4g}\t{w.nu:^5.4g}".format(w=w))

#>>> from sys import path; path.append('script'); from water import heat2flow, water
#>>> print(heat2flow(t1=90, t2=70, Q=64140))

'''>>> d = heat2flow(t1=12, t2=7, Q=1200)
>>> print(d)
Расход воды: 0.057 кг/с'''
