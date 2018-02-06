# Some new function and terms learned.
# To compare two sets:

# a = [1, 20, 3, 8, 5]
# b = [9, 8, 7, 6, 2, 9, 20]
# print set(a).intersection(b)
# #This works well. Return ans is set([8,20])
# # can also use
#
# print set(a) & set(b)
#
# #another option is :
#
# print [i for i, j in zip(a, b) if i == j]
# This code only works for equal sized lists and order is significant
# a = [1, 9, 3, 8, 5]
# b = [1, 9, 3, 8, 5]
#print [i for i, j in zip(a,b) if i ==j]
#zip function in strange for now.
# Just use cmp()

# print cmp(a,b)

# NOTE that cmp prints
# 0 if identical.
# +Ve if a is greater than b
# -Ve if b is greater than a.

# Note on Spliting Arrays:
x = [2,54,-6,7,35]

#   x[:1] = [2]. // returns first index and drops remaining indices
#   x[1:] = [54,-6,7,35]. // returns last indices and drops first index.
#   x[-1] = 35. //returns the last index "without the brackets[]", and drops the first indices
#   x[:-1] = [2,54,-6,7]. //reurns the first indexes and drops the last index.
#

# string.count(substring): returns number of occurrences of substring in string.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.

# Remember to use .find() function to find items in a list.
# Use the .append() function to add to a list.
# Declare a blank list first.
