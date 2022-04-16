"""

Passing functions to other functions
====================================

* Any function defined with the def construction can be passed
  as argument of other functions

Lambda functions
================

  >>> g = lambda arg1, arg2, arg3, ...: expression 
* Lambda functions are usually used to quickly define a function 
  as argument to another function.
* Lambda functions may also take keyword arguments.

"""
 
#%%
# Using a function defined with def
# This function only takes one argument
import math


def diff2nd(f, x, h=1E-6):
    '''diff2nd: computes second derivative of f in x'''
    
    r = (f(x-h) - 2*f(x) + f(x+h))/h**2
    return r

def g(t):
	return math.exp(t)*t**(-6)

t = 1.3
d2a = diff2nd(g, t)
print("g’’(%f) = %f" % (t, d2a))


#%%
# Using a lambda function:
g2 = lambda t: t**(6)
d2b = diff2nd(g2, 1.0, h=1E-4)
print(d2b)


#%%
# Using a lambda function in place:
d2c = diff2nd(lambda t: t**(-6), 1., h=1E-7)
print(d2c)


#%%
from math import exp

d2d = diff2nd(lambda t, A=1, a=0.5: -a*2*t*A*exp(-a*t**2), 1.2)
print(d2d)

d2d = diff2nd(lambda a, t=2, A=1: -a*2*t*A*exp(-a*t**2), 1.2)
print(d2d)


#%%




	



