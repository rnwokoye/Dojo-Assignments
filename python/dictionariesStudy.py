weekend = {"Sun": "Sunday", "Sat": "Saturday"}
capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

#to print all keys
for data in capitals:
     print data

print '#' * 50
#another way to print all keys
for key in capitals.iterkeys():
     print key

print '#' * 50
#to print the values
for val in capitals.itervalues():
     print val

print '#' * 50
#to print all keys and values
for key,data in capitals.iteritems():
     print key, " = ", data

print '#' * 50

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

for key, data in context.items():
    for value in data:
        print value['id'], value['content']

print '*' * 50

for data in context.values():
    for i in data:
        print i['id'], i['content']

print '*' * 50

# # def print_dictionary_values(dic):
# #     for some_key, some_value in dic.iteritems():
# #         print "My" + " " + some_key + " " + "is" + " " + str(some_value)
# #
# #         # alternate method:
# #         # concatenating variables to strings commonly done with the .format() method (can be used on any string, or variable that
# #         # contains a string
# #
# #         # print "My {} is {}".format(some_key, some_value)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
for names in students:
    print names['first_name'], names['last_name']

print '*' * 50

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for role in users:
    print role
    counter = 0
    for person in users[role]:
        counter+= 1
        first_name = person['first_name']
        last_name = person['last_name']
        str = len(first_name) + len(last_name)
        print "{} {} {} {}" .format(counter, first_name, last_name, str)

print '*' * 50

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def show_students(arr):
    for student in students:
        print student['first_name'], student['last_name']

def show_all(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)

show_students(students)
show_all(users)

print '&' * 50
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

# Lists from Dictionary
# It's possible to create lists from dictionaries by using the methods items(), keys() and values(). As the name implies the method keys() creates a list, which consists solely of the keys of the dictionary. While values() produces a list consisting of the values. items() can be used to create a list consisting of 2-tuples of (key, value)-pairs:

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
print my_dict.items()