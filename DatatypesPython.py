# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 00:36:12 2023

@author: Korisnik
"""

#5 data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries

myint = 5
myfloat = 5.2
mystr = "this is a string"        
mybool = True
mylist = [0,1,"two",3.2,False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2} 

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

myint = "abc"

print(mylist [3])
print(mytuple[1])
print(mylist [1:5])  #This is from the second to the sixth item
print(mylist[1:5:2])  #This is from the second to the sixth item while skipping the every second one
print(mylist[::-1])
print(mydict["one"])
print("String type" + "123")