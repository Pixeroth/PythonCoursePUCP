"""

Scopes of global vs local vars
==============================

* Variables assigned inside functions are local variables
* Local variables hide global variables.
* Local variables are invisible outside functions.

* Variables assigned outside functions are global variables
* Global variables can be accessed everywhere in a program, 
  also inside a function
* The values of global variables cannot be changed inside 
  functions unless the variable is declared as global
  
General rule:
Given a variable name, Python first tries to look up the variable 
name among the local variables, then among global variables, and 
finally among built-in Python functions.

"""

#%%
# global vars
a = 4
b = 5
c = 6
print(a*b)


#%%
# function with globals
def fn(a):
    #global c
    d = a
    a = b
    c = 9
    return a,b,c,d

print(a,b,c)
print(fn(b))    # modifies only global c 
print(a,b,c)
#print(d)  # error, since d scope is fn


#%%
# Example
# Defined globals in a function
g = 9.81

def yfunc(t, v0):
	return v0*t - 0.5*g*t**2

y = yfunc(t = 0.1, v0 = 6)
print(y)

g = 0
y = yfunc(t = 0.1, v0 = 6)
print(y)


#%%
# Example
# Undefined globals in a function
def yfunc(t):
	g = 9.81
	return x0 + v0*t - 0.5*g*t**2

x0 = 1    
v0 = 5
print(yfunc(0.6))

#%%
x0 = 0    
v0 = 0
print(yfunc(0.6))


#%%
