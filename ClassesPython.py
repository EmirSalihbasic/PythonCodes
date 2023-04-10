# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:21:54 2023

@author: Korisnik
"""

#classes in python          

class Vehicle ():
    def _init_(self, bodystyle):  #dont forget the space before first underscore
        self.bodystyle=bodystyle 

class Car (Vehicle):
    def __init__ (self, enginetype):    #Car() takes no arguments, add 2 underscores to solve this
        super()._init_("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

class Motorcycle (Vehicle):
    def __init__(self, enginetype, hassidecar):
        super()._init_("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
            self.doors = 0
            self.enginetype = enginetype

Car1 = Car ("gas")
Car2 = Car ("electric")
mc1 = Motorcycle ("gas", True)

print (mc1.wheels)
print (Car1.enginetype)
print (Car2.doors)