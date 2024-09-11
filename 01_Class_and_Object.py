#Employee is the class 
#__init__ is the constructor (dunder method) for initializing name,age,salary attribute
class Employee:
    def __init__(self, name, salary,age):
        self.name = name
        self.salary = salary
        self.age = age

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: ${self.salary}, Age: {self.age}"


    
# Creating objects or instances
employee1 = Employee("Sachin", 50000,40)
employee2 = Employee("Dhoni", 60000,35)

# Using methods
print(employee1.display_info()) 
print(employee2.display_info())  


