"""

Tuples are indicated by parentheses: (). Items in tuples can be
any other data type, including other tuples. Tuples are immutable,
meaning that once defined their contents cannot change.

"""

#%%
# define a tuple
mytup = ( "cesar", "augusto", 12, 12.3)


#%%
# membership and length
print(2 in mytup)
print(len(mytup))


#%%
# extract elements (0 -> 1st, 1 -> 2nd, ...)
print(mytup[2])
print(mytup[-1])


#%%
print(mytup[0:3])     # last item is not included, index 0 first elem, step 1
print(mytup[0:3:3])   # last item is not included, index 0 first elem, step 3
print(mytup[0::3])    # last item is included, index 0 first elem, step 3


#%%
# nested tuples
mytup2 = (mytup, mytup)
print(mytup2)
print(mytup2[1])

# using multiple index
print(mytup2[1][2])   


#%%
# concatenate tuples
print ((1, 2, 3) + (4, 5, 6))
print (mytup + mytup2)


#%%
# repeate tuples
print (('mouse',) * 4)      # comma is neccessary
print (('cat','dog') * 4)


#%%
# delete tuples
print('mytup2' in globals())
del(mytup2)   # also: del mytup2
print('mytup2' in globals())


#%%
# multi assigment with tuples
a, b, c = 1, 2, 3
print(a, b, c)


#%%
# internals
_t = (1, 2, 3)
a = _t[0]
b = _t[1]
c = _t[2]
print(a, b, c)


#%%
# swap
a, b = b, a
print(a, b)


#%% 
# the * operator for unpacking
a, b, *c = 1, 2, 3, 4, 5, 6, 7
print(a, b, c)




