#%% Dictionaries

emptyDictionary = {}
print("The value of emptyDictionary is:", emptyDictionary)


#%% create and print a dictionary with initial values
grades = { "John": 87, "Steve": 76, "Laura": 92, "Edwin": 89 }
print("\nAll grades:", grades)


#%% access and modify an existing dictionary
print("\nSteve's current grade:", grades[ "Steve" ])

grades[ "Steve" ] = 90
print("Steve's new grade:", grades[ "Steve" ])


#%% add to an existing dictionary
grades[ "Michael" ] = 93
print("\nDictionary grades after modification:")
print(grades)


#%% delete entry from dictionary
del(grades[ "John" ])
print("\nDictionary grades after deletion:")
print(grades)


#%% Dictionary methods
monthsDictionary = { 
    1 : "January", 2 : "February", 3 : "March", 
    4 : "April", 5 : "May", 6 : "June", 7 : "July", 
    8 : "August", 9 : "September", 10 : "October", 
    11 : "November", 12 : "December"}


#%%
print("\nThe dictionary keys are:")
print(monthsDictionary.keys())


#%%
print("\nThe dictionary values are:")
print(monthsDictionary.values())


#%%
print("The dictionary items are:")
print(monthsDictionary.items())


#%% Other useful methods

'''
clear()                             Deletes all items from the dictionary.

copy()                              Creates and returns a shallow copy of the dictionary .

get(key [, returnValue])            Returns the value associated with key. If key is not in the 
                                    dictionary and if returnValue is specified, returns the 
                                    specified value. If returnValue is not specified, returns None.

has_key(key)                        Returns 1 if key is in the dictionary; returns 0 if key is not 
                                    in the dictionary.

popitem()                           Removes and returns an arbitrary key-value pair as a tuple of 
                                    two elements. If dictionary is empty, a Key- Error exception 
                                    occurs.

setdefault(key [, dummyValue])      Behaves similarly to method get. If key is not in the dictionary 
                                    and dummyValue is specified, inserts the key and the specified 
                                    value into dictionary. If dummyValue is not specified, value is 
                                    None.

update(newDictionary)               Adds all key-value pairs from newDictionary to the current 
                                    dictionary and overrides the values for keys that already exist.

'''



















