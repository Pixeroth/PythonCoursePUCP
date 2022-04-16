#%% Scipy basic tutorial

# SciPy is a scientific ibrary for mathematics, science and engineering.

# The SciPy library depends on NumPy, which provides convenient and fast 
# N-dimensional array manipulation.

#%%
# Scipy subpackages
'''
scipy.cluster      Vector quantization / Kmeans
scipy.constants	   Physical and mathematical constants
scipy.fftpack	   Fourier transform
scipy.integrate	   Integration routines
scipy.interpolate  Interpolation
scipy.io	       Data input and output
scipy.linalg	   Linear algebra routines
scipy.ndimage	   n-dimensional image package
scipy.odr	       Orthogonal distance regression
scipy.optimize	   Optimization
scipy.signal	   Signal processing
scipy.sparse	   Sparse matrices
scipy.spatial	   Spatial data structures and algorithms
scipy.special	   Any special mathematical functions
scipy.stats	       Statistics

https://docs.scipy.org/doc/scipy/reference/index.html
'''

#%% 
# Optimization
import numpy as np
from scipy.optimize import brentq

# Example: finding roots
x = brentq(np.sin, 2, 4) 
print (x, x - np.pi)


#%%
# Integration
from scipy.integrate import simps
from scipy.integrate import quad

# Example: integrate from array using simpson
x = np.array([1, 3, 4])
y = x**2
print (simps(y, x))


#%%
# Example: integrate a function using gaussian quadrature
def sq(x):
	return x**2

print (quad(sq, 1, 4))


#%%
# Example: creating anonymus functions
print (quad(lambda x: np.exp(-x), 0, np.inf))


#%%
# Statistics
# import numpy as np
from scipy import stats

# Example: geometric and harmonic means
range20 = np.arange(1, 21)

print( "gmean: ", stats.gmean(range20))
print( "hmean: ", stats.hmean(range20))


#%%
# Linear Algebra

# scipy.linalg contains all the functions in numpy.linalg. plus some other 
# more advanced ones not contained in numpy.linalg.

# scipy.linalg is compiled with BLAS/LAPACK support.

# The scipy version might be faster depending on how numpy was installed.

# import numpy as np
from scipy import linalg

# Example: find the inverse
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
B = linalg.inv(A)
C = A.dot(B)

print( "identity:\n\n", C, end="\n\n" )
print( "determinant:\n\n", linalg.det(C) )


#%%
# Example solve matrix eq A X = B
A = np.array([ [-13,2,4], [2,-11,6], [4,6,-15] ])
B = np.array([5,-10,5])

x = linalg.solve(A,B)
print (A.dot(x))












