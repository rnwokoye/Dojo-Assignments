# import is used to make specialty functions available
# These are called modules
import random
import sys
import os

# Hello world is just one line of code
# print() outputs data to the screen
print("Hello World")

'''
This is a multi-line comment
'''

# A variable is a place to store values
# Its name is like a label for that value
name = "Derek"
print(name)

# A variable name can contain letters, numbers, or _
# but can't start with a number

# There are 5 data types Numbers, Strings, List, Tuple, Dictionary
# You can store any of them in the same variable

name = 15
print(name)

# The arithmetic operators +, -, *, /, %, **, //
# ** Exponential calculation
# // Floor Division
print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

# Order of Operation states * and / is performed before + and -

print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

# A string is a string of characters surrounded by " or '
# If you must use a " or ' between the same quote escape it with \
quote = "\"Always remember your unique,"

# A multi-line quote
multi_line_quote = ''' just
like everyone else" '''

print(quote + multi_line_quote)

# To embed a string in output use %s
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

# To keep from printing newlines use end=""
print("I don't like ",end="")
print("newlines")

# You can print a string multiple times with *
print('\n' * 5)

# LISTS -------------
# A list allows you to create a list of values and manipulate them
# Each value has an index with the first one starting at 0

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('The first item is', grocery_list[1])

# You can change the value stored in a list box
grocery_list[0] = "Green Juice"
print(grocery_list)

# You can get a subset of the list with [min:up to but not including max]

print(grocery_list[1:3])

# You can put any data type in a a list including a list
other_events = ['Wash Car', 'Pick up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]

print(to_do_list)

# Get the second item in the second list (Boxes inside of boxes)
print(to_do_list[1][1])

# You add values using append
grocery_list.append('onions')
print(to_do_list)

# Insert item at given index
grocery_list.insert(1, "Pickle")

# Remove item from list
grocery_list.remove("Pickle")

# Sorts items in list
grocery_list.sort()

# Reverse sort items in list
grocery_list.reverse()

# del deletes an item at specified index
del grocery_list[4]
print(to_do_list)

# We can combine lists with a +
to_do_list = other_events + grocery_list
print(to_do_list)

# Get length of list
print(len(to_do_list))

# Get the max item in list
print(max(to_do_list))

# Get the minimum item in list
print(min(to_do_list))

# TUPLES -------------
# Values in a tuple can't change like lists

pi_tuple = (3, 1, 4, 1, 5, 9)

# Convert tuple into a list
new_tuple = list(pi_tuple)

# Convert a list into a tuple
# new_list = tuple(grocery_list)

# tuples also have len(tuple), min(tuple) and max(tuple)

# DICTIONARY or MAP -------------
# Made up of values with a unique key for each value
# Similar to lists, but you can't join dicts with a +

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}

print(super_villains['Captain Cold'])

# Delete an entry
del super_villains['Fiddler']
print(super_villains)

# Replace a value
super_villains['Pied Piper'] = 'Hartley Rathaway'

# Print the number of items in the dictionary
print(len(super_villains))

# Get the value for the passed key
print(super_villains.get("Pied Piper"))

# Get a list of dictionary keys
print(super_villains.keys())

# Get a list of dictionary values
print(super_villains.values())

# CONDITIONALS -------------
# The if, else and elif statements are used to perform different
# actions based off of conditions
# Comparison Operators : ==, !=, >, <, >=, <=

# The if statement will execute code if a condition is met
# White space is used to group blocks of code in Python
# Use the same number of proceeding spaces for blocks of code

age = 30
if age > 16 :
    print('You are old enough to drive')

# Use an if statement if you want to execute different code regardless
# of whether the condition ws met or not

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')

# If you want to check for multiple conditions use elif
# If the first matches it won't check other conditions that follow

if age >= 21 :
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are old enough to drive a car')
else :
    print('You are not old enough to drive')

# You can combine conditions with logical operators
# Logical Operators : and, or, not

if ((age >= 1) and (age <= 18)):
    print("You get a birthday party")
elif (age == 21) or (age >= 65):
    print("You get a birthday party")
elif not(age == 30):
    print("You don't get a birthday party")
else:
    print("You get a birthday party yeah")

# FOR LOOPS -------------
# Allows you to perform an action a set number of times
# Range performs the action 10 times 0 - 9
for x in range(0, 10):
    print(x , ' ', end="")

print('\n')

# You can use for loops to cycle through a list
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y)

# You can also define a list of numbers to cycle through
for x in [2,4,6,8,10]:
    print(x)

# You can double up for loops to cycle through lists
num_list =[[1,2,3],[10,20,30],[100,200,300]];

for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

# WHILE LOOPS -------------
# While loops are used when you don't know ahead of time how many
# times you'll have to loop
random_num = random.randrange(0,100)

while (random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

# An iterator for a while loop is defined before the loop
i = 0;
while (i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        # Forces the loop to end all together
        break
    else:
        # Shorthand for i = i + 1
        i += 1
        # Skips to the next iteration of the loop
        continue

    i += 1

# FUNCTIONS -------------
# Functions allow you to reuse and write readable code
# Type def (define), function name and parameters it receives
# return is used to return something to the caller of the function
def addNumbers(fNum, sNum):
    sumNum = fNum + sNum
    return sumNum

print(addNumbers(1, 4))

# Can't get the value of rNum because it was created in a function
# It is said to be out of scope
# print(sumNum)

# If you define a variable outside of the function it works every place
newNum = 0;
def subNumbers(fNum, sNum):
    newNum = fNum - sNum
    return newNum

print(subNumbers(1, 4))

# USER INPUT -------------
print('What is your name?')

# Stores everything typed up until ENTER
name = sys.stdin.readline()

print('Hello', name)

# STRINGS -------------
# A string is a series of characters surrounded by ' or "
long_string = "I'll catch you if you fall - The Floor"

# Retrieve the first 4 characters
print(long_string[0:4])

# Get the last 5 characters
print(long_string[-5:])

# Everything up to the last 5 characters
print(long_string[:-5])

# Concatenate part of a string to another
print(long_string[:4] + " be there")

# String formatting
print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))

# Capitalizes the first letter
print(long_string.capitalize())

# Returns the index of the start of the string
# case sensitive
print(long_string.find("Floor"))

# Returns true if all characters are letters ' isn't a letter
print(long_string.isalpha())

# Returns true if all characters are numbers
print(long_string.isalnum())

# Returns the string length
print(len(long_string))

# Replace the first word with the second (Add a number to replace more)
print(long_string.replace("Floor", "Ground"))

# Remove white space from front and end
print(long_string.strip())

# Split a string into a list based on the delimiter you provide
quote_list = long_string.split(" ")
print(quote_list)

# FILE I/O -------------

# Overwrite or create a file for writing
test_file = open("test.txt", "wb")

# Get the file mode used
print(test_file.mode)

# Get the files name
print(test_file.name)

# Write text to a file with a newline
test_file.write(bytes("Write me to the file\n", 'UTF-8'))

# Close the file
test_file.close()

# Opens a file for reading and writing
test_file = open("test.txt", "r+")

# Read text from the file
text_in_file = test_file.read()

print(text_in_file)

# Delete the file
os.remove("test.txt")

# CLASSES AND OBJECTS -------------
# The concept of OOP allows us to model real world things using code
# Every object has attributes (color, height, weight) which are object variables
# Every object has abilities (walk, talk, eat) which are object functions

class Animal:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __name = None
    __height = None
    __weight = None
    __sound = None

    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def set_height(self, height):
        self.__height = height

    def set_weight(self, height):
        self.__height = height

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_height(self):
        return str(self.__height)

    def get_weight(self):
        return str(self.__weight)

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name, self.__height, self.__weight, self.__sound)

# How to create a Animal object
cat = Animal('Whiskers', 33, 10, 'Meow')

print(cat.toString())

# You can't access this value directly because it is private
#print(cat.__name)

# INHERITANCE -------------
# You can inherit all of the variables and methods from another class

class Dog(Animal):
    __owner = None

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        self.__animal_type = None

        # How to call the super class constructor
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print ("Dog")

    # We can overwrite functions in the super class
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(), self.get_height(), self.get_weight(), self.get_sound(), self.__owner)

    # You don't have to require attributes to be sent
    # This allows for method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 27, "Ruff", "Derek")

print(spot.toString())

# Polymorphism allows use to refer to objects as their super class
# and the correct functions are called automatically

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)


'''This is my notes on study of Python
VaRIABLE
Variable is a way to store a piece of data whcih can then be modofied at any time. eg "Spam = 5". Thus with
the variable "spam", we have stored the value 5. 
String can be any number letter or anything and it is in between quotes. A string can cotain letters, numbers or symbols. 
eg.: name = "Ryan"; age = "19"; food = "cheese". These are all strings.
Arithmetic operations are: % - returns the remainder of a division.
** makes exponential calculations.
// Performs a division and discards the remainder. '''
''' 
StRING
String methods lets you perform specific tasks on string. 4 types to learn now are:
len(); lower(); upper(); str()'''. Using the statement: parrot = Norweigian Blue
# len() give the lenth of charaters of a string. Usage is: print(len(parrot))
# Upper() and lower() covert the "case" of the letters. Usage: print(parrot.lower()); or print(parrot.upper())
#str() converts non-strings into strings by adding the quotes"" usage: str(parrot)
LiST
Sometimes we can use "lists" instead of strings. To use "lists", we put the string items in [] and use parenthesis for
each list item. Usage is thus: 
food_list = ["cake", "beans", "plantains", "eggs", "muffins"]
we can easily reference a list item thus: print(food_list[2]). This will print "plantains" from the list above.
we can also easily change a list item thus: food_list[1] = "rice". This changes the lits item "beans" to "rice". 
we can also print a subset of list items using colons(:) inside square brackets[] thus: print(food_list[1:3])
this will print "beans" and "plantains" from the food_list. (Note that it WILL NOT print list item 3.)
Lists can store numbers, strings, strings_and_numbers, and even other lists. eg:
numbers_list =["2", "10", "25", "50", "75"]
strings_list = ["cars", "boats", "planes", "trucks", "tickets"]
other_lists = [numbers_list, strings_list]. Note that we dont use parenthesis(" ") when storing lists within lists.
To add an item to a list, we use the "append" fucntion on the list declaration. Thus: 
numbers_list.append("100")
Note that when using the append function, you can ONLY append 1 item at a time. 
To remove an item from a list, use the (del) function before the list statement. Thus: 
del numbers_list[2]. This deletes "25" from the numbers list.
We can add 2 lists together using the + sign. thus: Print(list1 + list2).
We can set that to another list, eg: 
list3 = list1 + list2
print(list3).
TuPLES:
A tuple is a like a list without parenthesis " " eg. fibs = (0, 1, 1, 5, 3)
The main difference btw tupple and list is that you cannot reassign the values in a tuple.
so print(fibs[3]) would output "5".
however we cannot declare: fibs(3) = 10 to change the 4th item from 5 to 10, as we would in a list. 
MaP.
A map is a collections of things, like lists and tuples. The difference between maps and lists and tuples 
is that each item in a map has a "key" and a corresponding "value".
Consider this 'list' which stores some people and their favorite sports:
favorite_sports = ['Ralph Williams, Football', 'Michael Tippett, Basketball', 'Edward Edgar, Baseball', 'John Doe, Netball', 
'James Smith, Badmington', 'Frank Bridge, Rugby']
If stored in a map, it would be thus:
favorite_sports = { 
					'Ralph Williams' : 'Football', 
					'Michael Tippett' : 'Basketball', 
					'Edward Edgar' : 'Baseball', 
					'John Doe' : 'Netball', 
                    'James Smith' : 'Badmington', 
                    'Frank Bridge' : 'Rugby'
                    }
                    

                    
In a 'map', the person's 'name' (ie the key) is stored in between parentehsis(' '), and also the 'sport' (ie the value), and both seperated by a colon. The entire 'list' in enclosed in curly braces {}. The 'list' above, is a Map. (each key maps to a particular value)
To get a person's favorite sport, we print thus:
print(favorite_sport['John Doe']). This will return 'Netball' as his sport.
To delete: delete favorite_sport['John Doe']. 
To replace a 'value' in a map: favorite_sport['Ralph Williams'] = 'Ice hockey' This replaces "ice hockey" as Ralphs fav sport.
Note that in 'maps' we cannot join maps using (+) as we could with lists and tuples. 
Drawing With Turtles
To use "turtle", we have to use the python shell cmd and then create a canvas for the drawing thus:

>>> import Turtles			#This imports the turtle module
>>> t = turtle.Pen()		#creates the canvas
>>> t.forward(50)			#moves the pen 50 pixels fwd. 
>>> t.left(90)				#moves the pen 90 degrees to the left
>>> t.up()					#raises the pen off the canvas. No drawing while moving
>>> t.down()					#puts the pen down. Draws when moving
>>> t.right(90)				#moves the pen 90 degrees to the right
>>> t.backward(100)			#moves the pen 100 pixels backward. 
>>> t.clear()				#Clears the screen and leaves the turtle where it is.
>>> t.reset()				#resets screen and move turtle to starting point. 
NOTE that you can set the 'Pen()' variable to any letter of choice. so we can say: 
>>> import Turtles			#To import the Turtle module
>>> p = turtle.Pen()		# or (t) or (x) or (y) etc. 


IF Statements:
An 'if' statement is made up of the 'if' keyword; a condition; and a colon thus:
Symbols for conditions include: 
== (equal to )
!= (not equal to)
> ; <  (greater than ; less than)
>=; <= (greater than or equal to ; less than or equal to)
>>> age = 20
>>> if age >= 20:
		print('you are too old')		#This program would print 'you are too old'
		
Note that code following the 'if' statement must be in a 'block'.
A block is a grouped set of programming statements. 
in python, code that is in the same position, ie 'indented the same number of spaces, is grouped in a 'block'
Note that when using if; elif and else statements, we can conbine them in several ways thus: 
>>> age = 15
>>> if age == 10 or age == 11 or age == 12 or age == 13:      # combining conditions using 'or'. 
    >>> print('what is 13 + 49 + 84 + 155 + 97? A headache')
>>> if age >= 10 and age <=13: 
    >>> print('what is 13 + 49 + 84 + 155 + 97? A headache')    # combining conditions using 'and'
>>> elif age == 15:												# combining with elif
    print('that\'s a good age')
else:															# Combining with else 
    print('Huh...???')											# This condition prints 'Huh..??'
    
# "None" is used to assign a variable with no value. Thus:
>>> my_age = None
>>> print(my_age)
>>> None. 										# This is used to reset variables to their initial 'empty' state.

# Difference btw numbers and strings:
# User input in python is stored as a string. So an input of (10) in python will be stored as: ('10')
# We use the function (int) to convert this string into a number thus: 
>>> age = '10'
>>> converted_age = int(age)		# This will store the value 10 as a number. 
# Function (int) only works with integers. It cannot convert numbers (strings) with decimals. We use the function (float) to solve this problem. Thus:
>>> age = '10.5'
>>> converted_age = float(age)

# Weve already learned from past that we use the funtion str() to convert variables to strigs thus:
>>> age = 10
>>> converted_age = str(age)
>>> print(converted_age)
>>> '10'
Conditionals And Control Flow:
Control flow gives us this ability to choose among outcomes based off what else is happening in the program.
