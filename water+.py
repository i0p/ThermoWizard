Python 3.2.3 (default, Sep 10 2012, 11:22:57) 
[GCC 4.7.1] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> LMDT lambda t1, t2, t3, t4:
	
SyntaxError: invalid syntax
>>> LMDT lambda t1, t2, t3, t4: 1
SyntaxError: invalid syntax
>>> LMDT = lambda t1, t2, t3, t4: 1
>>> import math
>>> DT = lambda t1, t2 : t1 - t2
>>> DT(90,22)
68
>>> def LMDT(t1=90, t2=70, t3=22, t4=None):
"""температурный напор..."""
	t4 = t4 if t4 is not None else t3
	dt_in = DT(t1, t4)
	dt_out = DT(t2, t3)
	return (dt_in - dt_out)/math.log(dt_in/dt_out, math.e)

>>> LookupError
<class 'LookupError'>
>>> LMDT()
57.420659232575275
>>> LMDT(t2=85)
65.46818101862377
>>> 
