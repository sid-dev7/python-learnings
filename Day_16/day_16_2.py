class Person:
    pass
class Employee(Person):
    pass

class Manager(Employee):
    pass
print(f" base class for Manager = {Manager.__base__}")
print(f"base class for Employee = {Employee.__base__}")