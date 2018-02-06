#
# class Product(object):
#     def __init__(self, price, name, weight, brand):
#         self.price = price
#         self.name = name
#         self.weight = weight
#         self.brand = brand
#         self.status = "for sale"
#
#     def displayInfo(self):
#         print "Item Name: ", self.name
#         print "Brand: ", self.brand
#         print "Price + tax: $", self.price
#         print "weight: ", self.weight, "grams"
#         print "Item is ", self.status
#         return self
#
#     def sell(self):
#         self.status = "sold"
#         return self
#
#     def tax(self, tax):
#         self.price = self.price + self.price * tax
#         return self
#
#     def returnItem(self, reason):
#
#         if reason == "defective":
#             self.price = 0
#             self.status = "defective"
#
#         elif reason == "open_box":
#             self.status = "used"
#             self.price *= 0.80
#         else:
#             self.status = "for sale"
#             self.price = self.price
#         return self
#
#
#
# shoe1 = Product(100,'shoe',5,'Boss')
# car1 = Product(5000, 'car', 200, 'BMW')
# print "*" * 20
# shoe1.displayInfo().tax(0.2).sell().displayInfo()
# print "*" * 20
# shoe1.displayInfo().returnItem("open_box").displayInfo()
# shoe1.returnItem("defective").displayInfo()
# print "*" * 20
# shoe1.tax(.4).sell().displayInfo().returnItem("open_box").displayInfo()
# print "*" * 20
# shoe1.displayInfo()
# print "*" * 20
# car1.displayInfo().tax(.08).displayInfo().sell().displayInfo().returnItem("not_liked").displayInfo()

#
# class Vehicle(object):
#     def __init__(self, wheels, capacity, make, model):
#         self.wheels = wheels
#         self.capacity = capacity
#         self.make = make
#         self.model = model
#         self.mileage = 0
#     def drive(self,miles):
#         self.mileage += miles
#         return self
#     def reverse(self,miles):
#         self.mileage -= miles
#         return self
# class Bike(Vehicle):
#     def vehicle_type(self):
#         return "Bike"
# class Car(Vehicle):
#     def set_wheels(self):
#         self.wheels = 4
#         return self
# class Airplane(Vehicle):
#     def fly(self, miles):
#         self.mileage += miles
#         return self
# v = Vehicle(4,8,"dodge","minivan")
# print v.make
# b = Bike(2,1,"Schwinn","Paramount")
# print b.vehicle_type()
# c = Car(8,5,"Toyota", "Matrix")
# c.set_wheels()
# print c.wheels
# a = Airplane(22,853,"Airbus","A380")
# a.fly(580)
# print a.mileage
#
#
# def varargs(arg1, *args):
#    print "args is of " + str(type(args))
#
#
# varargs("one", "two", "three")


class MathDojo(object):
   def __init__(self):

      print "hello"
      x = 0
      y = 0

   def result(self):
      print x, y

      return self


   def add(self, x, y):
      x + y
      return self

   def subtract(self, x, y):

      return x - y

md =  MathDojo()

print md.add(2,10).subtract(5,2)

