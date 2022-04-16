# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 07:28:09 2021

@author: cague
"""

#%%
# read from a string
txt = "simple pleasures are the last resource of complex men"

# start empty dictionary
x = {}    

# accumulation main loop
for c in txt:
    if c not in x:
        # new character, initialize counter
        x[c] = 0

    # increment counter
    x[c] = x[c] + 1


print(x.items())


#%%
# below x == x.keys()
for k in sorted(x):
    print("{} appears {} times".format(k, x[k]))

print("------------", end="\n\n")


#%%    
for k in sorted(x, key=lambda k: x[k] ):
    print("{} appears {} times".format(k, x[k]))
    
print("------------", end="\n\n")

#%%    
for k in sorted(x, key=lambda k: x[k], reverse=True ):
    print("{} appears {} times".format(k, x[k]))    

print("------------", end="\n\n")


#%%
# find maximum frequency
keys = list(x.keys())
max_value = x[keys[0]]


for key in keys:
    if (x[key] > max_value):
        max_value = x[key]

print(max_value)


#%%
# Sorting a tuple: first sort by first element, if can't decide, go to
# the next element, and so on.

tups = [('A', 3, 2), ('C', 1, 4), ('B', 3, 1), ('A',2 ,4), ('C',1 ,2)]

for tup in sorted(tups):
    print(tup)

print("------------", end="\n\n")


#%%
# Using a tuple to sort a dictionary
# Sort fruits first by length, and then lexicografically:

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']

new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))

for fruit in new_order:
    print(fruit)
    
print("------------", end="\n\n")


#%%
# print the lenght in reverse order!
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))

for fruit in new_order:
    print(fruit)

print("------------", end="\n\n")
    

#%%
# When to use def vs lambda functions
# Here we have a dict, that for each state contains a list of 
# some of their cities:
states = {
            "Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
            "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
            "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]
            }

# Default sorting            
print(sorted(states))

print("------------", end="\n\n")


#%%
# Sort by the lenght of the first city string 
print(sorted(states, key=lambda state: len(states[state][0])))

print("------------", end="\n\n")


#%%
# Sort by number of cities that begin with capital S
def s_cities_count(cities_list):
    '''return a count of how many cities begin with 'S' '''
    ct = 0
    for city in cities_list:
        if city[0] == 'S':
            ct = ct + 1
    return ct
    
print(sorted(states, key=lambda state: s_cities_count(states[state])))
            
print("------------", end="\n\n")


#%%
def s_cities_count_for_state(state):
    cities_list = states[state]  
    return s_cities_count(cities_list)
    
print(sorted(states, key=s_cities_count_for_state))





