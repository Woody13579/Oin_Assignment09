#CoffeeClass.py
'''
Name: Drew Sexton
email: sextondw@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Description: This assignment shows that I work with a team on Github
'''

class Coffee():
    def __init__(self, size, blend, price):
        #print("Coffee.__init__()")
        self.size = size
        self.blend = blend
        self.price = price
    def print_size(self):
        print(self.size)
    def print_blend(self):
        print(self.blend)
    def print_price(self):
        print(self.price)
    def set_price(self,x):
        self.price = x
        print('Price = ' + str(x))
    def get_price(self):
        return str(self.price)
    def __str__(self):
        #print("Coffee.__str__()")
        return "size = " + str(self.size) + ", blend = " + str(self.blend) + ", price = " + str(self.price)
    def __repr__(self):
        #print("Coffee.__str__()")
        return str(self.size) + ", " + str(self.blend) + ", " + str(self.price)