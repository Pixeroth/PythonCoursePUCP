"""

Lists are indicated by square brackets: [ ]. Lists are pretty much the
same as tuples, but they are mutable: individual items in a list may be
changed. Lists can contain any other data type, including other lists.

"""

#%%
# define a list
lista = [1, 2, 3, 'a', 'b', (2, 3), ['2'] ]
print(lista)


#%%
# len and membership
print (len(lista), end='\n\n')          
print (2 in lista, end='\n\n') 
print (2 not in lista, end='\n\n')    


#%%
# print endings
print(2, end='\n\n')
print(3, end='\n\n')


#%%
# extract elements: 0 -> first element
print (lista[2], end='\n\n')
print (lista[-1], end='\n\n')


#%%
print (lista[0:3], end='\n\n')   # item 3 is not included
print (lista[0:6:2], end='\n\n') # item 6 is not included


#%%
# more about indexing
print (lista[2:-1], end='\n\n')  # -1 is not included
print (lista[2:], end='\n\n')    # -1 is included
print (lista[:], end='\n\n')     # all the list
print (lista[::3], end='\n\n')
print (lista[::-1], end='\n\n')  # reverse the list 


#%%
# is: check if two objects are the same in mem
# slicing always make a copy
import copy

A = [0, 5, [1, 2], [3, 4]]    
B = A[:]               # shallow copy: B = A.copy() or B = list(A)  
C = A                  # alias
D = copy.deepcopy(A)   # deep copy

print(B == A)
print(C == A)
print(D == A)
print(B is A)
print(C is A)
print(D is A)


#%% testing (replace D -> B, C)
D[2][1] = 10
print("A: ", A)
print("D: ", D)


#%%
# updating a list
lista[0] = 'h'
print (lista)


#%%
# update a slice
lista[0:7:3] = [10,10,10]
print(lista)

#%%
# extend and shrink a list
lista[2:2] = [1,2,3,4]
lista[3:5] = []
print(lista)


#%%
# deleting elements
del (lista[2])
print (lista)


#%%
# Concatenation and repetition
print ([1, 2, 3] + [4, 5, 6], end='\n\n')
print (['cesar'] * 4, end='\n\n')


#%%
# mutating methods: append, insert, remove, sort
lista.append('x')               # argument: elem
print (lista, end='\n\n')

lista.insert(2,'0')             # argument: pos, elem
print (lista, end='\n\n')

lista.remove('b')               # argument: elem
print(lista, end='\n\n')


lista2 = [5, 4, 10, 6, 0, 3, 2, 3, 1]

lista2.sort()
print(lista2, end='\n\n')

#%%
# non mutating methods: count, index
print(lista2.count(3), end='\n\n')      # argument: elem
print(lista2.index(3), end='\n\n')      # argument: elem


#%%
# other operations: sum, max, min
print(min(lista2))
print(max(lista2))
print(sum(lista2))


#%%
# Matrices? NOT list of lists
matrix = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
print(matrix[1][0])

# No good way for multiindex, no sum of matrices, etc.
# The best way of doing matrices in Python is to use the SciPy 
# or NumPy packages.

# this is ok
print(matrix[1:3])

# With "section" multi_index this should 
# output: [[5, 6], [8, 9]]
print(matrix[1:3][1:3])

# concatenation
print(matrix + matrix)


#%%
'''

Appendix: Lists methods
=======================

1	list.append(obj)            Appends object obj to list
2	list.count(obj)             Returns count of how many times obj occurs in list
3	list.extend(seq)            Appends the contents of seq to list
4	list.index(obj)             Returns the lowest index in list that obj appears
5	list.insert(index, obj)     Inserts object obj into list at offset index
6	list.pop(obj=list[-1])      Removes and returns last object or obj from list
7	list.remove(obj)            Removes object obj from list
8	list.reverse()              Reverses objects of list in place
9	list.sort([func])           Sorts objects of list, use compare func if given

Shallow vs deep copy
====================

https://www.geeksforgeeks.org/python-list-copy-method/

https://stackoverflow.com/questions/59025868/why-does-shallow-copy-behaves-as-deep-copy-for-a-simple-list
'''


