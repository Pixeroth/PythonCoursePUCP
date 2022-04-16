# Working with complexes

#%%
# define complexes
x = 2. + 3.j
y = 2. - 3.j

#%%
# operations
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)

#%%
# real, imag and abs
print (x.real + y.imag)
print (abs(y))  

#%%
# Using the cmath library
# In ipython try: cmath.<TAB>
import cmath

#%%
# Example 1
print(cmath.sin(x))
print(cmath.phase(x*y))

#%%
# Example 2
# Adding two phasors
v1 = cmath.exp(cmath.pi*1j)         # (-1,0)
v2 = cmath.exp((3/2.)*cmath.pi*1j)  # (0,-1)
v3 = v1 + v2                          # (-1,-1)

print("abs: ", abs(v3))
print("phase: ", cmath.phase(v3)*180/cmath.pi ) # in degrees









