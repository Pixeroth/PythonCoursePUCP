#%%
# Exact and long calculations

#%%
# exact computation
x = 4
y = 16
print ((x*y + x**y) * y/x )

#%%
# long integer calculation
print (x**y**x)
print (x**(y**x))
print ((x**y)**x)

#%%
# Using the Math library
# In ipython try: math.<TAB>
import math

# Example 1 
# important constants
print ('     pi = ', math.pi)
print ('      e = ', math.e)

#%%
# Example 2
# Density of sphere
d = 1.   # diameter (cm)
m = 5.   # mass (g)
v = (4./3.)*math.pi*(0.5*d)**3 # volume (cm**3)

print ("density = ", m/v, "g/cm**3")

#%%
# TODO
# - Change x and y to reals

#%%
'''
Appendix: The math library

* Basic functions

1	abs(x)              The absolute value of x: the (positive) distance between x and zero.
2	ceil(x)             The ceiling of x: the smallest integer not less than x
3	cmp(x, y)           -1 if x < y, 0 if x == y, or 1 if x > y
4	exp(x)              The exponential of x: ex
5	fabs(x)             The absolute value of x.
6	floor(x)            The floor of x: the largest integer not greater than x
7	log(x)              The natural logarithm of x, for x> 0
8	log10(x)            The base-10 logarithm of x for x> 0.
9	max(x1, x2,...)     The largest of its arguments: the value closest to positive infinity
10	min(x1, x2,...)     The smallest of its arguments: the value closest to negative infinity
11	modf(x)             The fractional and integer parts of x in a two-item tuple. Both parts 
                            have the same sign as x. The integer part is returned as a float
12	pow(x, y)           The value of x**y.
13	round(x [,n])       x rounded to n digits from the decimal point. Python rounds away 
                            from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.
14	sqrt(x)             The square root of x for x > 0


* Trigonometric functions

1	acos(x)             Return the arc cosine of x, in radians.
2	asin(x)             Return the arc sine of x, in radians.
3	atan(x)             Return the arc tangent of x, in radians.
4	atan2(y, x)         Return atan(y / x), in radians.
5	cos(x)              Return the cosine of x radians.
6	hypot(x, y)         Return the Euclidean norm, sqrt(x*x + y*y).
7	sin(x)              Return the sine of x radians.
8	tan(x)              Return the tangent of x radians.
9	degrees(x)          Converts angle x from radians to degrees.
10	radians(x)          Converts angle x from degrees to radians.


'''