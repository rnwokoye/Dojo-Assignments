
# OBJECT ORIENTED PROGRAMMING
#
# CLASS
# ATTRIBUTES
# METHODS
#
# INSTANCE/OBJECT
#
# PUBLIC/PRIVATE
#
# PROTECTED

#class User(object):
    #pass
# Create the class by keyword "class", then name of our class, and the parameter ("object")
# When the parameter for a class is "object, it simply means that this class inherits from the "object"
# class. Keyword 'pass' in the body is used as  a place holder and means do nothing.
#    michael = User()
#    ana = User()

class User(object):
    name = "Anna"


anna = User()
print "anna's name: ", anna.name
User.name = "Bob"
print "anna's name after change:", anna.name
bob = User()
print "bob's name:", bob.name
print User.name

