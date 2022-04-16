# Requesting input from the user

# input: input any user expression as a string
# eval:  evaluates any python string code

#%%
# Example 1: parse input using cast
# input always return a string
name = input("what is your name: ")

# the string can be parsed using casting
num_str = input("give me an integer number: ")
num = float(num_str) #eval(number)

# The difference between types are memory managment and operations
# that can be performed with them:
print ( "hi", name, "your number repeated is: ", num_str*2, \
	    "and your number duplicated is: ", num*2)


#%%
# Example 2: The command eval can be used instead of cast
# eval interprets the python code given as a string    
c = eval(input("give a complex number: "))  # try 1+1j

print("real part: ", c.real)
print("imaginary part: ", c.imag)
print("abs: ", abs(c))


#%%
# Example3: Multiple queries
# Alternative 1
#   Make the queries separately
a = float(input("Enter integer a: "))
b = float(input("Enter integer b: "))
c = float(input("Enter integer c: "))

#%%
# Alternative 2
#   Use eval to interprete the sequence of inputs (tuple), the input
#   data need to be separated by commmas
input_string = input( "Enter three integers (separated by commas): ")
a, b, c = eval(input_string)


#%%
# Alternative 3
#   Split the input by spaces, and cast each of the results using the
#   float command. 
input_string = input( "Enter three integers (separated by spaces): ")
a, b, c = map(float, input_string.split(";"))

















