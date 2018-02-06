print "This file is being loaded"

def test2():
	return "I am a test"

class Student(object):
	def __inint__(self, name):
		self.name = name

	def introduce(self):
		print "Hello my name is ", self.name
		