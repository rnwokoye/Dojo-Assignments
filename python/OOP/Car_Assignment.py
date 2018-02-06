class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax)


car1 = Car(3000, 60, "Full", 20)
car1.display_all()

car1 = Car(5000, 80, "Not Full", 20)
car1.display_all()

car1 = Car(10000, 60, "Kind of Full", 20)
car1.display_all()

car1 = Car(14000, 100, "Full", 20)
car1.display_all()

car1 = Car(9000.99, 120, "Empty", 20)
car1.display_all()

car1 = Car(12000.90, 60, "Empty", 20)
car1.display_all()



# Note the difference. Display ALL was part of the init statement. 
#WGoode Solution:
# OOP Car

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print 'Price: ' + str(self.price)
        print 'Speed: ' + str(self.speed) + 'mph'
        print 'Fuel: ' + self.fuel
        print 'Mileage: ' + str(self.mileage) + 'mpg'
        print 'Tax: ' + str(self.tax)


car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Empty', 15)
