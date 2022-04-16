# %%
# IO operations

# Open file modes
'''
Sintaxis

    f = open(file, mode)

    # file operations
    # ...

    f.close()

'r': Read mode allows you to read the fille. 
     You can't change it, only read it.

'w': Write mode will create the file if it does 
     not exist. If the file does exist, opening 
     it in 'w' mode will re-write it, destroying 
     the current contents.

'a': Append mode allows you to write onto the 
     end of a previously-existing file without 
     destroying what was there already.
'''

# %%
# Reading methods

'''
# read the file contents into a single string
string = FileHandle.read( ) 

# read the current line of the file into a string and advance the cursor to next line
line = FileHandle.readline( )

# read the file contents into a list of strings, one string for each line.
lines = FileHandle.readlines( )
'''

# %%
# read and write
import numpy as np

suma = np.pi + np.e

fileH = open("..\\data\\pi-e.txt", 'w')

fileH.write("pi = %6.4f \t e=%6.4f \n" % (np.pi, np.e))
fileH.write("pi + e = %6.4f \n" % suma)
fileH.close()


# %%
fileH = open("../data/pi-e.txt", 'r')

string = fileH.read()
print(string)
fileH.close()


# %%
# Read a numerical table
# Read all file as a string

# Example: read a three-column numerical data
# import numpy as np
fileH = open("../data/data-3-col.dat", 'r')

# all line a string
str1 = fileH.read()

# split at each: space, \n, \t
str2 = str1.split()

numbers1 = np.array([float(str_num) for str_num in str2])
numbers2 = np.reshape(numbers1, (3, numbers1.size//3))
numbers3 = np.reshape(numbers1, (numbers1.size//3, 3))

print(numbers2)
print(numbers3)
fileH.close()


# %%
# Read separated lines as strings

fileH = open("../data/data-3-col.dat", 'r')

# read all lines, each line is a string
lines_str = fileH.readlines()

# line_str: each string line
# number_str: each string number in line_str
numbers1 = np.array(
    [[float(number_str) for number_str in line_str.split()]
     for line_str in lines_str])

numbers2 = numbers1.transpose()

print(numbers1)
print(numbers2)

fileH.close()


# %%
# Using with to open and process file

with open("../data/data-3-col.dat", 'r') as file:
    # no need to read all lines first
    numbers1 = np.array(
        [[float(number_str) for number_str in line_str.split()]
         for line_str in file])

numbers2 = numbers1.transpose()

print(numbers1)
print(numbers2)

# no need to close the file


# %%
# Save numerical table to a file

# import numpy as np
fileH = open("../data/data3C-output.dat", 'w')

# numbers1 = ...

for row in numbers1:
    for column in row:
        fileH.write('%14.8f' % column)
    fileH.write('\n')

fileH.close()

# %%
# Numpy: loadtxt and savetxt
# Read numerical table

# import numpy as np

a = np.loadtxt('../data/data-3-col.dat')
print(a)


#%%
a = np.loadtxt('../data/data-3-col.dat', unpack=True)
print(a)

#%%
x, y, z = np.loadtxt('../data/data-3-col.dat', unpack=True)
print(x, y, z, sep='\n')


# %%
# Save numerical table

# import numpy as np
np.savetxt("../data/data3C-output2.dat", numbers1, fmt="%14.8f")


















