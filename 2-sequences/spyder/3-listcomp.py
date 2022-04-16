#%%
# Range and List Comprehensions


#%%
# Range of integers
axis = range(10)

print("\naxis list:", end=" ") 
print(list(axis))

print("\naxis tuple:", end=" ") 
print(tuple(axis))


#%%
# range third argument
evens = range(6, 18, 2)

print("\nevens list:", end=" ")
print(list(evens))

print("\nevens tuple:", end=" ")
print(tuple(evens))


#%%
# List comprehensions
# Sintaxis: [ f(i) for i in list ]

# Example 1
axis = [ 0.05*i for i in range(10) ]
print("\naxis:")
print(axis)


#%%
# Example 2
data = [2.1, 3.2, 6.7, 5.4, 1.2]
metric = [2.54 * measure for measure in data]
print("\nmetric:")
print(metric)


#%%
# Example 3
# set precision to 5 using numpy
import numpy as np
np.set_printoptions(precision=5)


#%%
axis = [ 0.312112*i for i in range(100)]
print("\naxis:")
print(np.array(axis))


#%%
data = [2.1, 3.2, 6.7, 5.4, 1.2]
metric = [2.54 * measure for measure in data]
print("\nmetric:")
print(np.array(metric))


#%%
# Example 4: Nested lists
pairs = [[1, 2], [2, 3], [3, 4], [4, 5]] 
sumpairs = [i + j for (i, j) in pairs]
print(sumpairs)


#%%
# Example 5: Using zip
list1 = list(range(5))
list2 = list(range(4, -1, -1))

print(list1)
print(list2)


#%%
pairs = [ (i, j, i + j) for i, j in zip(list1, list2)]
print(pairs)


#%%

