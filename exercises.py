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
print('{} {} {}'.format(emp2.first,emp2.last,emp2.pay))

print('\n')


# Class __init__

class EmployeeClass:
    num_of_employee = 0
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'
        
        EmployeeClass.num_of_employee +=1
        
    def fullName(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self): #but this is not an attribute
        self.pay = int(self.pay * self.raise_amount) 
        #or self.pay = int(self.pay * Employee.raise_amount) 
        
emp_1 = EmployeeClass('layth','Ele',80000)

emp_2 = EmployeeClass('Sam','Test',85000)
emp_3 = EmployeeClass('Sam','Test',85000)




print(emp_1.email)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(EmployeeClass.num_of_employee)



print(emp_1.fullName())
print(EmployeeClass.fullName(emp_1)) #exact same the result with this code  print(emp_1.fullName())


