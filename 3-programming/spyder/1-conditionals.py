"""
Conditionals
============

* Boolean type values: True, False
    * Values that behaves as False:
        * 0, or 0.0   (also 0L in old versions)
        * "" or '' (an empty string)
        * (), [], {} (The empty tuple, list, or dictionary)
    * Other values behaves as True
  
* Order relations: <, <=, >, >=, ==, !=

* Logical operators: and, or, not 
  
* pass: does nothing at all: it's only useful when you syntactically 
        need an indented suite, but don't want to do anything

"""

#%%
# bool function
print(bool([]))
print(bool(1.0))


#%%
# boolean expressions
print( "1:", not (3 > 2) and (5 < 1) )
print( "2:", not ((3 > 2) and (5 < 1)) )

print( "3:", 1.2 or [] ) 
print( "4:", 1.2 and [] )

print( "5:", 2 in [3, 4, 5, 6])
print( "6:", 5 in [3, 4, 5, 6])


#%%
# The if-else control structure
database = ( 'John', 'Eric', 'Albert', 'Graham', 'Terry', 'Michael')

name = input('Search user in database. Enter name: ')

if name in database:
    print("\n===>", name , "is a member of our database", end='\n\n')
else:
    print ("\n===>",'unknown member',end="\n\n")

print("=== END ===")


#%%
# The if-elif-else control structure
# Nesting control structures
# Example: conversion between qualifications
# https://es.wikipedia.org/wiki/Calificaci%C3%B3n_escolar

score = round(float(input("Enter score: ")))

if score < 5:
    letter = 'F'
    if score == 0: letter += '--'
    if score == 1: letter += '-'
    if score == 4: letter += '+'
elif score < 8:
    letter = "E"
    if score == 5: letter += '-'
    if score == 7: letter += '+'    
elif score < 11:
    letter ='D'
    if score == 8: letter += '-'
    if score == 10: letter += '+' 
elif score < 14:
    letter = 'C'
    if score == 11: letter += '-'
    if score == 13: letter += '+' 
elif score < 17:
    letter = 'B'
    if score == 14: letter += '-'
    if score == 16: letter += '+' 
else:
    letter = 'A'
    if score == 17: letter += '-'
    if score == 19: letter += '+'
    if score == 20: letter += '++'
    
print("Rounded score %d corresponds to "
     "letter qualification %s" % (score, letter) )
   
 
#%%    
'''

Logical operators
=================

and         If both the operands are true then condition becomes true.
or          If any of the two operands are non-zero then condition becomes true.
not         Used to reverse the logical state of its operand.


Membership
==========

in	        Evaluates to true if it finds a variable in the specified sequence 
                and false otherwise.
not in	    Evaluates to true if it does not finds a variable in the specified 
                sequence and false otherwise.

Identity operators
==================

is	        Evaluates to true if the variables on either side of the operator 
                point to the same object and false otherwise.	
is not	    Evaluates to false if the variables on either side of the operator 
                point to the same object and true otherwise.

Bitwise operators
=================

&           Binary AND - Operator copies a bit to the result if it exists in 
                both operands.
|           Binary OR - It copies a bit if it exists in either operand.
^           Binary XOR - It copies the bit if it is set in one operand but 
                not both.
~           Binary Ones Complement - It is unary and has the effect of 
                'flipping' bits.
<<          Binary Left Shift - The left operands value is moved left by 
                the number of bits specified by the right operand.
>>          Binary Right Shift - The left operands value is moved right by 
                the number of bits specified by the right operand.

'''







