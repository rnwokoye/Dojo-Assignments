class Bike(object):
    def __init__(self, price, max_speed):

        self.price = price
        self.max_speed = max_speed
        self.miles = 0


    def displayInfo(self):
        print "The Price is $ ", self.price
        print "Maximum speed ", self.max_speed, "mph"
        print "Total miles is ", self.miles, "miles"

    def ride(self):
        print "Riding"
        self.miles += 10


    def reverse(self):
        print "Reversing"
        if self.miles > 5:
            self.miles -= 5


Bike1 = Bike(200, 25)
Bike1.ride()
Bike1.ride()
Bike1.ride()
Bike1.reverse()
Bike1.displayInfo()

Bike2 = Bike(300, 15)
Bike2.ride()
Bike2.ride()
Bike2.reverse()
Bike2.reverse()
Bike2.displayInfo()


Bike3 = Bike(150, 5)
Bike3.reverse()
Bike3.reverse()
Bike3.reverse()
Bike3.displayInfo()



# # OOP Bike
#
# # define the Bike class
# class Bike(object):
#     def __init__(self, price, max_speed):
#         self.price = price
#         self.max_speed = max_speed
#         self.miles = 0
#
#     def displayInfo(self):
#         print 'Price is: $' + str(self.price)                 # Note use of "str" function
#         print 'Max speed: ' + str(self.max_speed) + 'mph'
#         print 'Total miles: ' + str(self.miles) + ' miles'
#
#     def drive(self):
#         print 'Driving'
#         self.miles += 10
#
#     def reverse(self):
#         print 'Reversing'
#         # prevent negative miles
#         if self.miles >= 5:
#             self.miles -= 5
#
# # create instances and run methods
# bike1 = Bike(99.99, 12)
# bike1.drive()
# bike1.drive()
# bike1.drive()
# bike1.reverse()
# bike1.displayInfo()
#
# bike2 = Bike(139.99, 20)
# bike2.drive()
# bike2.drive()
# bike2.reverse()
# bike2.reverse()
# bike2.displayInfo()









