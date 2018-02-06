# Find the occurence of an element in a string.

words = "It's thanksgiving day. It's my birthday,too!"                              #given string
words.find('day')                                                                   # Search for element 'day'
print words.find('day')                                                              # prints result to screen


# Replace an element in a string

print words.replace('day', 'month')                                                 #replaces "day" with 'month' and prints to screen.

# Prnt the Min and Max Value.

x = [2,54,-2,7,12,98]                                                               #given list
y = [19,2,54,-2,7,12,98,32,10,-3,6]


def minMax(list):                                                                  #function declaration
    minimum = min(list)                                                             #finds the minimum of given list
    maximum = max(list)                                                             #finds the max of given list
    print 'min number is: ', minimum, 'maximum number is: ', maximum                  #Prints the minimum and maximum values of list

minMax(x)                                                                           #function call using 'x' and 'y' given list
minMax(y)




# First And Last
x = ["hello",2,54,-2,7,12,98,"world"]

first_val = x[:1]
last_val = x[-1]
print(first_val, last_val)

# SortList
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x)/2]                                                           # optional first parameter of slice defaults to zero
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list