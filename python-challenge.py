'''
Created on 7 Jun 2022

@author: laythal-shblawi
'''


                                       ########## Python Principles Challenging website##########
                                       
                                       
                                       
                                       
                                       
                                      ####https://pythonprinciples.com/lessons/Lists/###########
   
#List in Python

#Change the code so that the returned list also contains the number 5 after the number 4.

def get_numbers():
    add = [5]   
    return [1,2,3,4]+ add 

print(get_numbers())

###########################################

#Make sure that the list returned by get_laundry also contains the string "shorts".

def get_laundry():
    
    add = ["shorts"]
    laundry = ["shirts", "socks", "pants"]
    return laundry + add

print(get_laundry())

###########################################

#Write a function, zero_one, that returns a list containing the numbers 0 and 1 in order.

def zero_one():
    my_list=[0,1]
    return my_list
print(zero_one())

###########################################

#Write a function, get_mix, that returns a list where:

#the first element is the boolean False
#the second element is the integer 1
#the third element is the string `"three"

def get_mix():
    my_list = [False, 1,'three']
    return my_list
print(get_mix())

###########################################

#List Comprehension: Elegant way to create Lists

pow2 = [2 ** x for x in range(10)]
print(pow2)

pow2 = []
for x in range(10):
   pow2.append(2 ** x)
print(pow2)   

###########################################

#A list comprehension:if statement

pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

odd = [x for x in range(20) if x % 2 == 1]
print(odd)



