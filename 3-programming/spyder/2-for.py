'''

For loop keywords
=================

else:       code that is done only if the for loop exits normally (no breaks)

continue:   goes straight to the next iteration of the for loop
break:      causes Python to abandon the loop 
pass:       does nothing at all: it's only useful when you syntactically 
                need an indented suite, but don't want to do anything

'''

#%%
# iterating over tuples and lists
for x in (1, 2, 3): print(x)


#%%
for x in (1, 2, 3): print(x, end='')


#%%
for x in [1, 2, 3]: print(x, end=' ')  


#%%
# Iterate over range object
# Using continue
for j in range(10):
    if j == 5:
        continue
    print(j)


#%%
# Using break
n = 10
for j in range(1, n+1):
    if j == 5:
        break
    print(j)


#%%
# Using pass
n = 10
for j in range(1, n+1):
    if j == 5:
        pass
    print(j)


#%%    
# Generate a list from an empty list
lista = []
for i in range(10):
    c = i*0.25
    lista.append(c)
    print(lista)


#%%
# Allocating memory for a list
N = 10
lista = [None] * N   # Null contents
for i in range(N):
    lista[i] = i*0.25
    print(lista)


#%%
# Enumerations
# Convert to list or tuples
lista2 = [3,6,9,12,15]
print(list(enumerate(lista2)))
print(tuple(enumerate(lista2)))


#%%
# Modify a list using enumaration
for i,c in enumerate(lista2):
    print(i,c)
    lista2[i] = c * c
print(lista2)


#%%
# Using zip to loop over two pairs
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 6, 9, 12, 15]
lista = []

for x, y in zip(lista1, lista2):
    print(x, y)
    lista.append((x, y, x + y, x*y))    
print(lista)


#%%
# Nested loops
mainlist = []

for x in lista1:
    sublist = []
    for y in lista2:
        sublist.append((x, y, x + y))
    mainlist.append(sublist)
print(mainlist) 

#%%
lista3 = [(1, 2), (3, 4), (5,6)]

for tup in lista3:
    for value in tup:
        print(tup, value)


#%%
# A cummulative sum
n = 10
sum = 0

for j in range(1, n+1):
    sum = sum + j
    print(sum)
print("sum of", n, "first integers is", sum)


#%%
# A cummulative product
n = 5
prod = 1

print("partial prods:", end=" ")
for j in range(1, n+1):
    prod = prod * j
    print(prod, end=" ")
print("\nfact(", n, ") =", prod)


#%%
# Nested control structures
# Example: Compute prime numbers less than 100
NMAX = 100
primes = []

for n in range(2, NMAX):
    for x in range(2, n):
        if n % x == 0:
            #print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        # print(n, 'is a prime number')
        primes.append(n)
print(primes)


#%%
'''


Traversing nested lists
=======================

1 iter -> [-, ....]
2 iter -> [[-, ...], [-, ...], ...]
3 iter -> [[[-, ...], [-, ...], ... ], [[-, ...], [-, ...], ... ], ...]
....


# loop over lists directly
for sublist1 in somelist:
    for sublist2 in sublist1:
        for sublist3 in sublist2:
            for sublist4 in sublist3:
                value = sublist4
                # work with value


# loop over indexes
for i1 in range(len(somelist)):
    for i2 in range(len(somelist[i1])):
        for i3 in range(len(somelist[i1][i2])):
            for i4 in range(len(somelist[i1][i2][i3])):
                value = somelist[i1][i2][i3][i4]
                # work with value

'''
