#%%
# List Comprehensions
# Sintaxis: [ f(i) for i in list ]

#%%
# Range of integers: using range
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
# List comprehensions examples

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
# Example 3: Nested lists
pairs = [[1,2], [2,3], [3,4], [4,5]] 
sumpairs = [i + j for i,j in pairs]
print(sumpairs)


#%%
# Example 4: Using zip
list1 = list(range(5))
list2 = list(range(4, -1, -1))

print(list1)
print(list2)

#%%
pairs = [ (i,j) for i,j in zip(list1,list2)]
print(pairs)



