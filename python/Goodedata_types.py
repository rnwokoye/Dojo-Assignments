a = [1,2,"abacus"]
b = {
	"name": "Example McExampleface", 
	"email": "example@example.com"
}
c = (1.0, 2, 3)
d = 1, True
e = {
	"thing1": a, 
	"thing2": b, 
	"thing3": (a,b,c)
}

"""
Guess what each print statement will say
"""

# print type(a)
# print type(a[1])
# print type(a[2])
# print type(b)
# print type(b["name"])
# print type(c)
# print type(c[0])
# print type(d)
# print type(d[1])
# print type(e)
# print type(e["thing1"])
# print type(e["thing1"][2])
# print type(e["thing2"])
# print type(e["thing3"])
# print type(e["thing3"][3])
# print type(e["thing3"][2])

# print e["thing1"][0], e["thing2"]["name"], e["thing3"][0]

'''
for element in e:
	# print element
	for thing in e[element]:
		print thing
'''