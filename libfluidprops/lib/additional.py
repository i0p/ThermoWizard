#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  additional.py
#
#  @Copyright: 2016 by iop <iop@com.ny>
#
#  @license: GNU GPL, see COPYING for details.



"""
Doc this module

samples this module
"""

class cached_property(object):
	def __init__(self, func):
		self.func = func
	def __get__(self, instance, cls=None):
		result = instance.__dict__[self.func.__name__] = self.func(instance)
		return result
	def __set__(self, instance, value):
			raise AttibuteError("readonly attribute")

if __name__ == "__main__":
  import doctest
  doctest.testmod()
