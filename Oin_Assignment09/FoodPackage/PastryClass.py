# CoffeeClass
'''
Name: Oin
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This is the entry point for our group code
'''
class Pastry():            
    def setPrice(self, price):
        self.validatePrice(price)
    def validatePrice(self, price):
        if price > 10:
            print ("Price of pastry should not be that high!")
        else:
            self.price = price  
            
    def setType(self, type):
        self.validateType(type)
    def validateType(self, type):
        typeList = ["Croissants", "Coffee Cake", "Muffin", "Scone", "Donut" ]
        if type not in typeList:
            print ("We don't sell that pastry here")
        else:
            self.type = type   
    #  without a barcode.
    def __init__(self, barcode, name, price, type):
        self.barcode = barcode  # store the barcode in the current object
        self.validatePrice(price)
        self.validateBrand(type)
        
    def __repr__(self):
        #return a string representation of the object.
        return "barcode = " + self.barcode+ ", " + str(self.price) + ", " + str(self.type)
    
    def __str__(self):
        #return a 'pretty' string representation of the object
        return "barcode = " + self.barcode + ", " + str(self.price) + ", " + str(self.type)

