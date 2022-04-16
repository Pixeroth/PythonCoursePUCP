#!/usr/bin/env python
# coding: utf-8

# # Numpy fast tutorial

# In[]:
# ### Default behavour of lists

# not quite useful multi-indexig
# not optimized for numerical array computing
# mutability has effects on performance in genera

M = [[1, 2], [3, 4]]

print( M * 3 )
print( M + M )
# print(M * M)    # give an error


# In[ ]:
# ### Numpy array creation

# numpy extends the functionality
# also numpy arrays are faster and use less memory
import numpy as np 


# In[ ]:
# Define a 1-dim array
M = np.array([1 ,2, 3])

print(M.ndim)
print(M.size)
print(M.shape)
print(M.dtype)
print(M.itemsize)


# In[ ]:
# Define a 2-dim array
M = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print(M.ndim)
print(M.size)
print(M.shape)
print(M.dtype)
print(M.itemsize)


# In[ ]:
# Define a 3-dim array
M = np.array( [ [ [1, 2], [3, 0] ], [ [3, 4], [5, 0] ], [ [4, 5], [6, 0] ] ] )

print(M.ndim)
print(M.size)
print(M.shape)
print(M.dtype)
print(M.itemsize)


# In[ ]:
# Copy the array, casting to a given type.
N = M.astype(np.int64)

print(N.ndim)
print(N.size)
print(N.shape)
print(N.dtype)
print(N.itemsize)


# In[ ]:
# Use dtype argument to specify the type
M = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]], dtype=np.float64)

print(M.ndim)
print(M.size)
print(M.shape)
print(M.dtype)
print(N.itemsize)


# In[ ]:
# ### Array copy vs alias
# https://numpy.org/doc/stable/reference/generated/numpy.copy.html

M = np.array([[1 ,2, 3], [3, 4, 5], [4, 5, 6]])
N2 = np.array([[0 ,0, 0], [0, 0, 0], [0, 0, 0]])

# Alias: same array
N1 = M            
print(N1 is M)

# Views: similar to "shallow copy" for lists
N2 = M[:]         
print(N2 is M)    # N2 is a new array, with shared content

N3 = M.view()     
print(N3 is M)    # N3 is a new array, with shared content

# Copies: similar to "deep copy" for lists
# See example about object type in doc:
# https://numpy.org/doc/stable/reference/generated/numpy.copy.html

N4[:] = M         # copy contents of M into N4
print(N4 is M)     # N4 pre-exists and has same dims

N5 = np.copy(M)   
print(N5 is M)    # N5 is a new array

N6 = M.copy()     
print(N6 is M)    # N6 is a new array

# Do changes and print output: 
N2.shape = (1,9)
N2[0, 0] = 100
N5[1, 1] = 200

print('alias:')
print(M, N1, sep='\n\n')

print('\nviews: ')
print(N2, N3, sep='\n\n')

print('\ncopies: ')
print(N4, N5, N6, sep='\n\n')


# In[ ]:
# ### Convert input to array

# array: by default will make a copy of the object 
# asarray: will not unless necessary (for example changing type)

# For tuples and list asarray make a copy
a = ((1, 2), (2, 3), (4, 5))
print(np.asarray(a) is a)

a = [[1, 2], [2, 3], [4, 5]]
print(np.asarray(a) is a)


#%%
# For ndarrays asarray make a copy when necessary
a = np.array([[1, 2], [2, 3], [4, 5]])
print(np.asarray(a) is a)

a = np.array([[1, 2], [2, 3], [4, 5]])
print(np.asarray(a, dtype=np.int64) is a)


#%%
# Example
m = np.array([1, 2, 3]);
p = np.array(m)
q = np.asarray(m)

m[0] = 4               # change first element
print(m, p, q, sep='\n\n')

m = np.append(m, 4)    # append makes a copy
print(m, p, q, sep='\n\n')

# In[ ]:
# ### Reshaping an array

P = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# reshape: does not modify original array
m = P.reshape(6,2)
print('-----', P, m, sep ='\n')

# resize: modify the original array
n = P.resize(6,2)
print('-----', P, n, sep ='\n')

P[0] = 100
print('-----', P, m, n, sep ='\n')


# In[ ]:
# ### Flattening and array

P = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# flatten makes a copy of the original
f = P.flatten()
print('-----', f, sep ='\n')

# ravel makes a view
r = P.ravel()
print('-----', r, sep ='\n')

P[0] = 100
print('-----', P, f, r, sep='\n')

# In[ ]:
# ### Automatic construction

print (np.arange(0, 1, 0.25), end ='\n\n')
print (np.arange (0, 1.01, 0.25), end ='\n\n')

print (np.linspace(0, 1, 5), end ='\n\n')
print (np.logspace(0, 3, 4), end ='\n\n')

print (np.zeros([2, 3], np.int32), end ='\n\n')
print (np.ones([2, 3], np.int32), end ='\n\n')

print (np.zeros([2, 3], np.double), end ='\n\n')
print (np.ones([2, 3], np.double), end ='\n\n')

# In[ ]:
# ### Vectorization

# vectorizes other internal functions
M = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print(3 * M, end ='\n\n')
print(M + M, end ='\n\n')
print(M * M, end ='\n\n') # array multiplication
print(M**2,  end ='\n\n')
print(M**M,  end ='\n\n')
print(np.sin(M))       


# In[ ]:
# ### Math operations

print(M.min(), end ='\n\n')
print(M.max(), end ='\n\n')
print(M.sum(), end ='\n\n')
print(M.sum(axis=0), end ='\n\n')
print(M.sum(axis=1), end ='\n\n')
print(M.prod(), end ='\n\n')
print(M.prod(axis=0), end ='\n\n')
print(M.prod(axis=1), end ='\n\n')

# In[ ]:
# ### Array indexing

M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(M[1], end ='\n\n')
print(M[1][2], end ='\n\n')
print(M[1, 2], end ='\n\n')

# In[ ]:
# Colon operator: ini:end:step
    
print(M)
print(M[0:2, 2], end ='\n\n')
print(M[0, :2], end ='\n\n')
print(M[:, 2], end ='\n\n')
print(M[::2, 2], end ='\n\n')
print(M[:2, :2], end ='\n\n')

# In[]:
# Slices of arrays returns views of the original data. 
# Different from list or tuple slicing

N = M[::2, ::2]
print(N, end ='\n\n')

M[0] = 100
print(M, N, sep='\n')

# In[ ]:
# Advanced indexing: with integer or boolean arrays

# Advanced indexing always returns a copy of the data.

# Indexing with integer array
v = np.array([0, 2, 0, 2])
print(M)
print(M[v, 2], end ='\n\n')
print(M[2, v], end ='\n\n')
print(M[v, v], end ='\n\n')


# In[ ]:
# In the last example M[v, v] don't produce a matrix as in other
# languages. In numpy the sintaxis would be:  
r = np.array([[0, 0], [2, 2]])
c = np.array([[0, 2], [0, 2]])
print(M)
print(M[r, c], end ='\n\n')


# In[ ]:
# Indexing with boolean array
N = M > 4
print(M, end ='\n\n')
print(N, end ='\n\n')
print(M[N], end ='\n\n')


# In[ ]:
# Example
x = np.array([[1., 2.], [np.nan, 3.], [np.nan, np.nan]])
print(x, end ='\n\n')
print(x[~np.isnan(x)], end ='\n\n')


# In[ ]:
# Assigning values to indexed arrays
M[::2, 2] = 10
print(M, end ='\n\n')


#%%
M[r, c] = 100
print(M, end ='\n\n')


#%%
M[r, c] = np.array([[1, 0], [0, 1]])
print(M, end ='\n\n')


# In[ ]:
# ### Basic linear algebra

#%% Transposition
M = np.array([[0, 2, 3], [3, 4, 0], [4, 0, 6]])
print(np.transpose(M))
print(M.T)

#%% Matrix multiplication
print(np.matmul(M, M))
print(M @ M)             # equivalent to matmul
print(np.dot(M, M))      # Also valid with scalars
print(M.dot(M))

#%% Cross products
print(np.cross(M, M))  # Multiple cross-products (vector1 * vector-1, ...)
print(np.cross(M, M.T))

#%%
# inverse, det and eig
# from numpy import linalg -> linalg.inv(M)
print(np.linalg.inv(M), end='\n\n')  
print(np.linalg.det(M), end='\n\n')
print(np.linalg.eig(M), end='\n\n')


# In[ ]:
# Solve matrix eq A X = B

# Matrix of coefficients
A = np.array([ [-13, 2, 4], [2, -11, 6], [4, 6, -15] ])

# inhomogeneous vector
B = np.array([5, -10, 5])

# solution
print (np.linalg.solve(A, B))


# In[ ]:
# ### Array printing

# set precision using numpy (5 decimals)
np.set_printoptions(precision=5)

data = [2.1, 3.2, 6.7, 5.4, 1.2]

metric = [2.54 * measure for measure in data]
print("\nmetric:", np.array(metric), end ='\n\n')


# In[ ]:
axis = [ 0.312112*i for i in range(100)]
print("axis:")
print(np.array(axis), end ='\n\n')


# In[ ]:
np.set_printoptions(linewidth=80, formatter={'float_kind': "{:>15.3f}".format})

print("axis 2:")
print(np.array(axis))


# In[ ]:
np.set_printoptions(linewidth=80, formatter={'float_kind': lambda x: f'{x:>15.2f}'})

print("axis 2:")
print(np.array(axis))


# In[ ]:
np.set_printoptions(linewidth=80, formatter={'float_kind': lambda x: "%15.2f"%(x) })

print("axis 2:")
print(np.array(axis))










