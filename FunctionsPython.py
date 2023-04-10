# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 23:50:14 2023

@author: Korisnik
"""



def main ():
    print ("Hello World!")
    name = input ("What is your Name?")
    print ("Nice to meet you, Sir")
    
if __name__ == "__main__":      #It executes the main() function only if this file is executed as the main program.
    main()
        


def somefunction():
    global mystr 
    mystr = "def"
    print(mystr)
    
somefunction()
print(mystr)

del mystr
print (mystr)


# define a function

def func1():
    print("I am a function")


    
func1()
print(func1())
print(func1)  
    
#function that takes arguments

def func2(arg1, arg2):
    print(arg1,"  " ,arg2)
    
 
    
#function that returns the value

def cube(x):
    return x * x * x


func2(10, 20)
print(func2(10,20))
print(cube(3))   



#function with default value for an argument

def power (num, x=1):
    result = 1
  
    for i in range (x):
        result = result * num
        return result


print (power(2))
print(power(2,3))
print(power(x=3, num=2))

#function with variable number of arguments

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print( multi_add (4,10,5,4))
print (multi_add (4,10,5,4,10))