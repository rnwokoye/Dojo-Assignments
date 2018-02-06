'''This is my beginning study of python. I will import the modules random;
sys; and OS. This is according to the tutorial '''
import random
import sys
import os


quote = "\"always remember you are unique.\""
print(quote)
# A multi_line_quote
multi_line_quote = ''' just
like everyone else" '''
my_variable = 10
print(my_variable)
count_to = 10+100
print(count_to)
print("The addition is", count_to)
count_to = 5**3
print('The addition is', count_to)
modulo = 5 % 4
print(modulo)
python = 4
berry = python ** 2
print(berry)
berry = "pythons"
print(berry)

ceasar = "Graham"
print(ceasar)
car_list = "['benze','BMW','rover']"
print(car_list[2])
print(car_list.upper())

my_home = "house"
print(len(my_home))
s = "Whereof one cannot speak, thereof one must be silent."
print(s)
len(s)

s.lower()
print(s.upper())
print (s.lower())
parrot = " Norwegian Blue"
print(len(parrot))
print(len(s))
print(parrot.lower())
print(parrot.upper())
print(len(parrot))
print(parrot.lower())

pi = 3.14
print(pi)
print(str(pi))
ministry = "The Ministry of Silly Walks"
print(str(ministry))
print(ministry.upper())
print("s " + "parrot")
print(s)
print(parrot)
print(s + parrot)

print("spam " + "and " + "eggs")
print("The value of pi is 3.14")
print("the value of pi is around " + str(3.14))
print("the value of a car worth around " + str(5000))
car = 5000
print(car)
string_1 = "Camelot"
string_2 = "place"
print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
from datetime import datetime
now = datetime.utcnow()
print(now)
current_year = now.year
current_month = now.month
current_day = now.day
print(now)
print(current_year)
print(now.year)
print("%s / %s / %s" % (now.year, now.month, now.day))
print("%s:%s:%s" %(now.hour, now.minute, now.second))
fred = '''how do dinosaurus pay their bills
using Tyranosaurus dollars'''
print(fred)
text = ''' This multi line string isn't so bad after all. "I love it much more than before". '''
print(text)
single_quote_str = 'He said "Aren\'t, can\'t, shouldn\'t, wouldn\'t"'
double_quote_str = "He said \"Arent't can't shouldn't wouldn't\""
print(single_quote_str)
print(double_quote_str)
# message = "I scored"
message = "score"
print(message)
print(message)
