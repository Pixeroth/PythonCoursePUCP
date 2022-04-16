# Using Modules

#%%
# Import cmath library
import cmath
print (cmath.pi)


#%%
# Import all functions from cmath
# Not recommended
# from cmath import *
# print (cos(pi))


#%%
# Import cmath with a different namespace
import cmath as cm
print (cm.pi)
print (cm.sin(cm.pi))


#%%
# Import specific functions from cmath
from cmath import pi, sin
print (pi)
print (sin(pi))


#%% 
# Import specific functions from cmath
from cmath import pi as pi1, sin as sin1
print (pi1)
print (sin1(pi1))


#%%
# Unified treatment of complex and real functions
from math import sqrt as sqrt1
print(sqrt1(4))
print(sqrt1(-1))


#%%
from cmath import sqrt as sqrt2
print(sqrt2(4))
print(sqrt2(-1))  


#%% Mathematical functions with automatic domain
# numpy.sqrt returns NaN for negative numbers
from numpy.lib.scimath import sqrt as sqrt3
print(sqrt3(4))
print(sqrt3(-1))  


#%% Equivalent functions in scipy
from scipy import sqrt as sqrt4
print(sqrt4(4))
print(sqrt4(-1))  


#%%
# Example: the quadratic formula
a = 1; b = 2; c = 100 # polynomial coefficients
r1 = (-b + sqrt3(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt3(b**2 - 4*a*c))/(2*a)
print(r1, r2)


#%%
a = 1; b = 4; c = 1 # polynomial coefficients
r1 = (-b + sqrt3(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt3(b**2 - 4*a*c))/(2*a)
print('r1 = {:.10f}  \nr2 = {:.10f}'.format(r1,r2))



#%%