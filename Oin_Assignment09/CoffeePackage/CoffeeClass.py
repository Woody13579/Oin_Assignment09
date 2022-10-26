#CoffeeClass.py
'''
Name: Drew Sexton
email: sextondw@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Description: This assignment shows that I work with a team on Github
'''

class Coffee(drink):
    def __init__(self, size, blend, price):
        print("Coffee.__init__()")
        self.size = size
        self.blend = blend
        self.price = price
        super().__init__(type)
    def print_size(self):
        print(self.size)
    def print_blend(self):
        print(self.blend)
    def print_price(self):
        print(self.price)
    def __str__(self):
        print("Coffee.__str__()")
        return super().__str__() + ", size = " + self.size + ", blend = " + self.blend + ", price = " + self.price
     