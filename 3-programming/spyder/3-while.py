"""

While loop keywords
===================

else:       code that is done only if the for loop exits normally (no breaks)

continue:   goes straight to the next iteration of the for loop
break:      causes Python to abandon the loop 
pass:       does nothing at all: it's only useful when you syntactically 
                need an indented suite, but don't want to do anything

"""


#%%
# iterating over a list
lista = [2,4,6,8,10]
index = 0
while(index < len(lista)):
    print(lista[index])
    index += 1


#%%
# create a list which its size is not known in advance 
lista2 = []

from random import randint
r = randint(0,9)
print(r)

while ( r >= 1 ):
    lista2.append(r)
    r = randint(0,9)
    print(r)
print(lista2)


#%%
# Example: Check whether a number is prime. 
number = int(input ("Enter integer to check: "))
print()

if number%2 == 0: 
    if number == 2: 
        print(number, "is a prime.")
    else:
        print(number, "is not a prime.")
else:
    iterator = 3
    while iterator < number :
        if number%iterator == 0 :
            print(number, "is not a prime.")
            break
        else:
            iterator += 2
    else:
        print(number, "is a prime.")


#%%
# Example: Guess a computer generated random number
import random

NMAX = 1000000
guess = 0

computer_number = int(NMAX * random.random()) + 1

while guess != computer_number:
    guess = int(input("Enter your guess (<=0 to quit): "))
    if guess > 0:
        if guess > computer_number:
            print("Number too large")
        elif guess < computer_number:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")
    
    

#%%

'''

Appendix 1: Assignment operators
================================

+=      c += a is equivalent to c = c + a
-=      c -= a is equivalent to c = c - a
*=      c *= a is equivalent to c = c * a
/=      c /= a is equivalent to c = c / a
%=      c %= a is equivalent to c = c % a
**=     c **= a is equivalent to c = c ** a
//=     c //= a is equivalent to c = c // a


Appendix 2: random module
=========================

choice(seq)             A random item from a list, tuple, or string.
randrange([i,] e [,d])  A randomly selected element from range(i, e, d)
random()                A random float r, such that 0 is less than or equal 
                            to r and r is less than 1
seed([x])               Sets the integer starting value used in generating 
                            random numbers. 
shuffle(lst)            Randomizes the items of a list in place.
uniform(x, y)           A random float r, such that x is less than or equal 
                            to r and r is less than y


Generate random intergers from random
=====================================
    
random() elem [0,1)

* {0, 1}    -> int(random.random() + 0.5)            
* {-1, 1}   -> 2 * int(random.random() + 0.5) - 1
* {1,...,N} -> int(N * random.random()) + 1

'''




