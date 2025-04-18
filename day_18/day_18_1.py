class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def print_info(self):
        print(f"name = {self.__name}")
        print((f"age  = {self.__age}"))
Person = Person('person 1', 10)
Person.print_info()