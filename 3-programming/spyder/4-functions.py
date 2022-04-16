'''

Defining functions 
==================

* Functions are defined using the def statement:

    def function_name(arg1, arg2, ...):
        body_of_function

* Functions can have any number of arguments.

* The statement return [expression] exits a function, optionally 
  passing back an expression to the caller.

* Functions can return any number of expressions: 
    return expr1, expr2 ...

* Functions can return any values at all. In this case just avoid 
  the return statement, put a return statement with no arguments 
  or equivalently return None

* The first statement of a function can be an optional statement - 
  the documentation string of the function or docstring.

* Positional arguments vs keyword arguments:  
  * def somefunc(arg1, arg2, kwarg1=val1, kwarg2=val2):
      
  * arg1, arg2 are positional arguments
  
  * kwarg1, kwarg2 are keyword or named arguments
  
  * The keyword arguments must always be listed after the positional 
    arguments in the function definition.
    
  * Keyword arguments that do not appear in the call get their
    values from the specified default values.
    
'''


#%%
# sign function
def signf(x):
    if x >= 0:
        return 1
    else:
        return -1

print(signf(5))
print(signf(-5))


#%%
# factorial function
def factorial(n):
    ''' 
    This function calculates n!
    '''
    f = 1
    for i in range(2,n+1):
        f = f * i
    return f

#print(help(factorial))

print(factorial.__doc__)

print ('\n%10s %10s' % ('n', 'n!'))
for j in range (10) :
    print ('%10d %10d' % (j, factorial(j)))


#%%
# Example: "Pass by Object Reference"

# If you pass immutable arguments like integers, strings or tuples 
# to a function, the passing acts like call-by-value. 
# They can't be changed within the function, because they can't be 
# changed at all, i.e. they are immutable. 

def foo(a):
    a = 4
    print(a)
    
a = 2
foo(a)
print(a)

#%%
# If we pass mutable arguments, they are also passed by object reference, 
# but they can be changed in place within the function.
 
# If we pass a list to a function, we have to consider two cases: 
# - Elements of a list can be changed in place. 
# - If a new list is assigned to the name, the old list will not be affected.

def bar(a):
    a[1] = -2
    print(a)
    
a = [2,4,5]
bar(a)
print(a)

#%%
# Example: define isPrime(n) that returns true if n	is							
# a prime. Make a list of the first 100 primes
def isPrime(n):
    '''
    Gives true if n is a prime number and false otherwise.
    '''
    if n == 2 or n == 3: return True
    if n%2 == 0 or n<2: return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd numbers
        if n%i == 0:
            return False    
    return True

count = 0
number = 2
NMAX = 100
primes = []

while count < NMAX :
    if isPrime(number) : 
        primes.append(number)
        count = count + 1 		
    number = number + 1
print(primes)


#%%    
# Optional arguments
# Example: The damped oscillator formula
from math import pi, exp, sin

def f(t, A=1, beta=1, omega=2*pi):
    return A*exp(-beta*t)*sin(omega*t)

# Tests
v1 = f(0.2)
v2 = f(0.2, omega=1)
v3 = f(1, A=5, omega=pi, beta=pi**2)
v4 = f(A=5, beta=2, t=0.01, omega=0.1)
v5 = f(0.2, 0.5, 1, 1)      # positional

print(v1, v2, v3, v4, v5, sep="\n")
    


