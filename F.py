# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:49:03 2019

@author: 郭思淼
"""


from math import *
class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w
    def value(self, x):
        return exp(-self.a*x)*sin(self.w*x)

#test
f = F(a=1.0, w=0.1)
print(f.value(x=pi))
f.a = 2
print(f.value(pi))



        