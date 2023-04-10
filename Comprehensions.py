# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 03:25:02 2023

@author: Korisnik
"""
#list comprehension


#filters and transforming the elements of the list

#%(modules operator) gives us remain after 

numbers_list = [0 , 1 , 2, 3 , 4, 5, 6, 7, 8, 9]

doubled = [x*2 for x in numbers_list]

print(doubled)
evens = [x for x in numbers_list if x % 2 == 0]   #after we divide the number with 2, and remain is 0, so basically, even numbers
print (evens)


#2
myList = list(range(100))
filtered_list = [x for x in myList if x % 10 == 0]
print(filtered_list)

#3

myList = list(range(100))
filtered_list = [x for x in myList if x % 10 < 3]
print(filtered_list)

#4

myList = list(range(100))
filtered_list = [x for x in myList if x % 10 == 3]
print(filtered_list)

#5

squares = []
for i in range (1, 11):
    squares.append(i**2)  #numbers from 1 to 10 squared


#6 this is more readable
squares = [i**2 for i in range (1,11)]   #

#7 list of squares, only those divisible by 4

squares = [i**2 for i in range (1,11) if i**2 % 4 == 0] 
print (squares)

#8 capitals
capitals_by_country = {'UK':'London', 'France':'Paris', 'Germany':'Berlin'}
countries_by_capital = {capital: country for country, capital in capitals_by_country.items()}
print(countries_by_capital)

#9 sum the squares from 1**2 to 10**2
sum (i**2 for i in range (1,11))

#10 nested comprehensions
counting = []

for i in range(1, 11):
    for j in range(1, i+1):
        counting.append(j)
        
print(counting)        


# nested comprehension
counting = [j for i in range(1, 11) for j in range(1, i+1)]

print(counting)
