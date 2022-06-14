'''
Created on 9 Jun 2022

@author: laythal-shblawi

'''

# Classes in Pythoin


class Employee:

    pass

emp1= Employee()
emp2 = Employee()



emp1.first = 'Layth'
emp1.last = 'ele'
emp1.pay = 80000
emp1.email = 'layth.ele@gmail.com'


emp2.first = 'sam'
emp2.last = 'leo'
emp2.pay = 85000
emp2.email = 'test@gmail.com'

print(emp1.first +' '+ emp1.last)
print(emp2.pay)
print('\n')


# Class __init__

class EmployeeClass:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'
        
emp_1 = EmployeeClass('layth','Ele',80000)
emp_2 = EmployeeClass('Sam','Test',85000)

print(emp_1.email)
print(emp_2.pay)









