# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 01:21:25 2023

@author: Korisnik
"""

# list
fruits = ['orange', 'apple', 'banana', 'kiwi', 'apple']

print(fruits)
print(len(fruits))  #length
print(fruits[1:4])
print(fruits[0])
print(fruits[-1])


del fruits[1]
print(fruits)

fruits2 = fruits + ["Watermelon"]
print (fruits2)

fruits2.remove ("Watermelon")
print (fruits2)

# mutable
fruits.append('grape')
print(fruits)

fruits.sort()
print (fruits)

fruits.pop(2)
print(fruits)

fruits.append(fruits[1])
print(fruits)

fruits.extend(fruits[2])
print(fruits)


a = fruits[0]
b = fruits[1:] 
fruits3 = [a]
fruits2.extend(['Grape'])
fruits3.extend(b)
print(fruits3)

reverse_fruits3= sorted(fruits3, reverse=True)
print(reverse_fruits3)


# tuple
a = (1, 2, 3)

singleton = (1, )
b = (1,) * 5

b.count(1)
a.index(2)


(x,y,z) = ('a','b','c')
print(x)

data  = (1,2,3)
x, y, z = data
print(x)

(x,y) = (y,x)

# Dictionary

capitals = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
print(capitals)
print(capitals['Italy'])

morecapitals = {'Spain': 'Madrid','Germany': 'Berlin'}

capitals.update (morecapitals)
print(capitals)


Dict = {'Lily':35,'Jack':20, 'Tom':40}
print(Dict)
Dict = dict([('Lily', 35), ('Jack', 20), ('Tom', 40)])
print(Dict)

Dict['Jack']


print(Dict.keys())
print(Dict.values())

# nested dictionary
Dict = {1:'Lily',2:'Jack',3:{'A':'Welcome', 'B':'to', 'C':'NEOMA'}}
print(Dict[3]['B'])
print(Dict[3]['C'])

Dict[1]
print(Dict[3]['A'])
print(Dict[3]['B'])
print(Dict[3]['C'])

print(Dict[1]+Dict[3]['A']+Dict[3]['B']\
      +Dict[3]['C'])
    
# Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('Blueberry' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)   

a - b # difference
a | b # union
a & b # intersection
a ^ b # letters in a or b but not both

print((a | b) - (a & b))

#union attribute for set (tuple and list dont have this attribute)

a = {"Lyon","Marseille"}
b = {"Reims","Strasourg"}
c = a.union(b)

print(c)
