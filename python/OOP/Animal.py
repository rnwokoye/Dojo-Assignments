class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def walk(self):
        self.health -= 1
        return self


    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "The Animal named {} health is {} ".format(self.name, self.health)
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self



class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name,health)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "I am a Dragon named {} my health is {}".format(self.name, self.health)
        return self




animal1 = Animal("Thingy1",20)

animal1.walk().walk().walk().run().run().displayHealth().run().displayHealth()

animal2 = Animal("Thingy2", 5)

animal2.walk().walk().run().run().run().displayHealth().run().displayHealth()

animal3 = Dog("Dog1", 10)

animal3.walk().walk().walk().run().run().pet().displayHealth()

animal4 = Dragon("Dragon1", 50)

animal4.walk().fly().displayHealth().fly().displayHealth()



