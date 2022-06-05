'''
Created on 4 Jun 2022

@author: laythal-shblawi
'''

from _operator import length_hint
from turtle import Shape

#Hello World program 

print("Hello World!")

#########################


# #Class exercise 

class Animal:
    eyes=2
    def talk(self):
        return("Animal talk")

class Dog(Animal):
    legs=4
    def talk(self):
        return("wooooooof")
    
shiba=Dog()

print("Shiba has "+str(shiba.eyes)+" eyes")
print("Shiba has "+str(shiba.legs)+" legs")
print("Shiba says "+shiba.talk() )

###########################

#Using __init__ class to calculate the Square shape 

class Shape:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
        
    def area(self):
        return self.length*self.length
    def perimeter(self):
        return self.width*4
    
        
l= int(input("Enter the Square length : "))
w= int(input("Enter the Square width : "))


square=Shape(l,w)
print("the square Area is : "+ str(square.area()))
print("the square Perimeter is : "+ str(square.perimeter()))

        
        
    
    
    
    
