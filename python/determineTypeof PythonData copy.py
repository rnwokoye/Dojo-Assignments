#To get the type of an object, you can use the built-in type() function. Passing an object as the only parameter will return the type object of that object:

#For this note, check out :
# String functions
# List Functions
# Tuple functions.
# See how these sets of data are manipulated


def dataType():

    type([]) is list

    type({}) is dict

    type('') is str

    type(0) is int


a = Test1()
b = Test2()

    isinstance(a, Test1)

>>> isinstance(b, Test1)
True
>>> isinstance(b, Test2)
True
>>> isinstance(a, Test1)
True
>>> isinstance(a, Test2)
False
>>> isinstance([], list)
True
>>> isinstance({}, dict)
True

>>> some_list = [1, 2, 3]
>>> some_list[-1] = 5 # Set the last element
>>> some_list[-2] = 3 # Set the second to last element
>>> some_list
[1, 3, 5]

#TUPLE Functions:
# len(sequence):
# max(sequence) returns the largest value in the sequence
# sum(sequence) return the sum of all values in sequence
# enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence

# cmp(dict1, dict2) - Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the two dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
# len() - give the total length of the dictionary.
# str() - produces a string representation of a dictionary.
# type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dictionary type.
# Python includes the following dictionary methods:
# (either dict.method(yourDictionary) or yourDictionary.method() will work)
#
# .clear() - removes all elements from the dictionary
# .copy() - returns a shallow copy dictionary
# .fromkeys(sequence, [value] ) - create a new dictionary with keys from sequence and values set to value.
# .get(key, default=None) - For key key, returns value or default if key is not in dictionary.
# .has_key(key) - returns true if a given key is available in the dictionary, otherwise it returns false.
# .items() - returns a list of dictionary's (key, value) tuple pairs.
# .keys() - return a list of dictionary keys.
# .setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
# .update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary.
# .values() - returns list of dictionary values.
