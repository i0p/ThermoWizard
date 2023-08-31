#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  fluidProps.py
#
#  @Copyright: 2017 by iop <iop@com.ny>
#
#  @license: GNU GPL, see COPYING for details.

import sys
from libfluidprops.HEOSProps import TIFPoint

"""
def Q(p1, p2, L):
	Qt = L*(1/p1.Vha)*(p1.H-p2.H)/3600
	Qs = L*(1/p1.Vha)*p1.C*(p1.T-p2.T)/3600
	return Qt, Qs
>>> CD1 = t2 = HWAPoint(T=T(23.3),R=0.50)
>>> CD2 = HWAPoint(T=T(37.3),W=CD1.W)
>>> Q(CD1,CD2, 1450)
(-6836.970802300389, -6774.671363402909)
"""

def main(foo): pass
#    HXChart()
#	return 0

if __name__ == "__main__": sys.exit(main(sys.argv))
