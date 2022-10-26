# TeaClass
'''
Name: Aaron Wood
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This is a class for our group code
'''

class Tea():       
    def __init__(self, type, price):
        self.type = type;
        self.price = price;
             
    def setPrice(self, x):
        self.price = x
        print('New price is ' + str(x))
        
    def getType (self):
        return str(self.type) + " Tea"
    
    def salesTax (self):
        return "Price with Sales Tax : " + str(self.price * 1.007)
        
    def __repr__(self):
        return str(self.type) + ", " + str(self.price)
    
    def __str__(self):
        return "Type : " + str(self.type) + ", Price : " + str(self.price)
