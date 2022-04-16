# Defining variables 

#%% Basic ussage
x = 2
y = 3
z = x + y

print(z**2)

# redefine don't update dependencies
x = 5
print(z)


#%% delete variables
del x, y, z

#%%
# Ejemplo 1:
# Swaping variables
x, y = 2, 3
x, y = y, x

print ("x =", x)
print ("y =", y)

#%%
# Ejemplo 2:
# Positions at time t in free fall 
g = 9.8
vo = 5
t = 10
print ("position: ", vo*t + 0.5*g*t**2, "m")

