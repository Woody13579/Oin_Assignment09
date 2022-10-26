# Main
'''
Name: Oin Group
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This is the entry point for our group code
'''

from CoffeePackage.CoffeeClass import *
from FoodPackage.PastryClass import *
from TeaPackage.TeaClass import *

# Calling Pastry Class
Pastry = Pastry(1, 3, 'Scone')
print(Pastry.__str__())
print(Pastry.__repr__())
Pastry.setPrice(11)
Pastry.setType('Apple')

print('====================')

# Calling Tea Class
Tea = Tea('Black', 3)
print(Tea.__str__())
print(Tea.__repr__())
Tea.setPrice(5)
print(Tea.getType())
print(Tea.salesTax())

print('====================')

# Calling Coffee Class
Coffee = Coffee('Large', 'Dark Roast', 6)
print(Coffee.__str__())
print(Coffee.__repr__())
Coffee.set_price(10)
print(Coffee.get_price())


