# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:24:30 2023

@author: Korisnik
"""

People = [('Albert','Einstein', '10'),
           ('Nikola','Tesla', '15'),
            ('Thomas','Edison','10')]

People [0][0]

People [0]

People [0][1]

[person for person in People if person[2] == '10']  #this is simillar to where clause in sql




import collections

persontype = collections.namedtuple('person', ['firstname', 'lastname', "birthday"])
emir= persontype("Emir", "Salihbašić", "February 21")
emir = persontype(lastname ="Salihbašić",firstname="Emir",birthday="February 21")
print(emir)

emir[0]
emir[1]
emir[2]
emir[0],emir[1],emir[2]
emir.firstname, emir.lastname, emir.birthday




#Dataclass
# !pip install dataclasses
from dataclasses import dataclass

class personclass:
      firstname: str 
      lastname: str
      birthday: str = 'unknown'
    
emir = personclass('Emir', 'Salihbašić')    

print(emir)



emir = personclass('Emir', 'Salihbašić')    
emir.firstname, emir.lastname, emir.birthday


class Personclass:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Personclass("Emir",29)

print(p1.name)
print(p1.age)