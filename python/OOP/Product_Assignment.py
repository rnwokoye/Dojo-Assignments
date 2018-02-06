class Product(object):
    def __init__(self, item_name, brand, price, weight):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
        self.displayInfo()


    def sell(self):
        self.status = "Sold"
        return self.status


    def tax(self, tax):
        self.price = (self.price * tax) * self.price
        return self.price

    def returnItem(self, reason):
        if (reason == "defective"):
            return self.reason
        return self.price

    def displayInfo(self):
        print "Item Name: ", self.item_name
        print "Brand: ", self.brand
        print "Price: $", self.price
        print "weight: ", self.weight, "grams"






Item1 = Product("Phone", "Apple", 2000, 20)


# class Product(object):
#     def __init__(self, Price, Item_Name, Weight, Brand, status):
#         self.Price = Price
#         self.Item_Name = Item_Name
#         self.Weight = Weight
#         self.Brand = Brand
#         self.Status = status
#
#
#     def sell(self):
#         self.status = "Sold"
#         return self.status
#
#
#     def tax(self, tax):
#         self.price = (self.price * tax) * self.price
#         return self.price
#
#     def returnItem(self, reason):
#         if (reason == "defective"):
#             return self.reason
#         return self.price
#
#     def displayInfo(self):
#         print self.price
#         print self.item
