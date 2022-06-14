'''
Created on 4 Jun 2022

@author: laythal-shblawi
'''
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



#Functions

#Program that check the leap year ^_^

     #numbeers of days per month , first value placeholer for indexing purpose
month_days = [0,30,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    #return true for leaps year , false for non-leap years 
    
    return 'Is this leap year ? :' , year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

  
def days_in_month (year, month):
    #reture nummber of days in that month in that year
    
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month ==2 and is_leap(year):
        
        return 'This month has', 29,'days'

    return 'This month has' ,month_days[month],'days'


print(is_leap(2024))
print(is_leap(2023))
print(is_leap(100024))
print(days_in_month (2000, 2))
print(days_in_month (2000, 4))







        
        
    
    
    
    
