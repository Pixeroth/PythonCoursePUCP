# Casting data types

# Function	              Description
#===============================================================
# int(x)	Converts x to an integer
# long(x)	Converts x to a long integer
# float(x)	Converts x to a floating point number
# str(x)	Converts x to an string. x can be of the type float, 
#           integer or long.
#
# hex(x)	Converts x integer to a hexadecimal string '0x....'
# oct(x)	Converts x integer to a octal string '0o....'
# bin(x)	Converts x integer to a binary string '0b....'
#
# chr(x)	Converts integer ASCII code x to a character
# ord(x)	Converts character x to integer ASCII code


#%%
# casting to integer
a = 10.9
a1 = '10.9'
print(a, type(a), a1, type(a1))

b = int(a)
b1 = int(float(a1))
print(b, type(b), b1, type(b1))


#%%
# casting to float
c = 20
c2 = '20'
print(c, type(c), c2, type(c2))

d = float(c)
d2 = float(c2)
print(d,type(d), d2, type(d2))


#%%
# casting to string
user = "cesar"
lines = 37

print("Congratulations, " + user + "! You just wrote " + \
	str(lines) + " lines of code.")


#%%









