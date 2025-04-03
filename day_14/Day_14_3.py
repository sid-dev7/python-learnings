class Address:
    def __init__(self, city, state, country):
        self.__city = city
        self.__state = state 
        self.__country = country 
    def  print_address(self):
        print(f"city = {self.__city}")
        print(f"state = {self.__state}")
        print(f"country = {self.__country}")

class person:
    def __init__(self, name, city, state, country, age):
        self.__name = name 
        self.__age = age
        self.__address = Address(city, state, country) 
    def print_info(self):
        print(f"***personal details***")
        print(f"name = {self.__name}")
        print(f"age = {self.__age}")
        self.__address.print_address()
        print("-" * 40)

p1 = person('person1', 'pune', 'MH', 'India', 10)
p1.print_info()
p2 = person('person2', 'Mumbai', 'MH', 'India', 22)
p2.print_info()

class House:
    def __init__(self,owner,city,state,country):
        self.__owner = owner 
 
    def print_info(self):
        print(f"***house details***")
        print(f"owner = {self.__owner}")
        print("-"*40)

p1 = person('person1','pune','MH','India',10)
print(p1.__dict__)
p1.print_info()
# h1 = House('owner1','mumbai', 'MH', 'India')
# h1.print_info()
