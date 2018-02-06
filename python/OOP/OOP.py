#sdahal1 : Rob github page

class Human(object):
    def __init__(self, name, height, weight):
        print "creating a human"
        self.name = name
        self.height = height
        self.weight = weight
        self.health = 100

    def verbalattack(self, target):
        print "aargh"
        target.health -= 10

awesomeStudent1 = Human ("Kap", 1, 2)
awesomeStudent2 = Human ("Jef", 1, 2)

# print awesomeStudent1.name
# awesomeStudent2.verbalattack(awesomeStudent1)
# print awesomeStudent1.health


class Warrior(Human):
    def __init__(self, name, height, weight, strength):
        super(Warrior, self).__init__(name, height, weight)
        print "we are creating a warrior"
        self.strength = strength
        self.health *= 2

    def verbalattack(self, target):
        #target.health = 0
        # or if them warrior attacks twice:
        target.health = target.health - 20
        return self

warrior1 = Warrior ("steph curry", 1000, 1, 100)
print warrior1

warrior1.verbalattack(awesomeStudent2).verbalattack(awesomeStudent1)
print awesomeStudent2.health
print awesomeStudent1.health












