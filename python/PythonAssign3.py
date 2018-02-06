
def filterByType(var):
    if var >= 100:
        print 'That\'s a big number'
    elif var < 100:
        print 'That\'s a small number'

filterByType(455)


def filterByType(str):
    if len(str) >= 50:
        print 'Long sentence'
    elif len(str) < 50:
        print 'Short sentence'

filterByType('doyouhavetheDojo')
filterByType('Tell me and I forget. Teach me and I remember. Involve me and I learn')

def filterByType(list):
    if len(list) >= 10:
        print 'Big list'
    elif len(list) < 10:
        print 'Short list'

filterByType(['name','address','phone number','social security number'])
filterByType([4,34,22,68,9,13,3,5,7,9,2,12,45,923])