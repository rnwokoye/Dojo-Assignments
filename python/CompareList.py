
#list_one = [1,2,5,6,2]
#list_two = [1,2,5,6,2]

#list_one = [1,2,5,6,5]
#list_two = [1,2,5,6,5,3]

#list_one = [1,2,5,6,5,16]
#list_two = [1,2,5,6,5]

#list_one = ['celery','carrots','bread','milk']
#list_two = ['celery','carrots','bread','cream']


list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

a = list_one
b = list_two

def compList():
    if cmp(a,b) == 0:
        print "The lists are the same"
    else:
        print "The lists are not the same"

compList()


