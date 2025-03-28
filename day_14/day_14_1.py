class person:
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age
    def print_info(self):
        print(f"name = {self.__name}")
        print(f"address = {self.__address}")
        print(f"age = {self.__age}")
#person.__init__(p1, name='person1',address='Pune', age= 20)
p1 = person(name='person', address ='Pune', age=20)
# person.print_info(p1)
p1.print_info()

#person.__init__(p2, name='person2',address='Mumbai', age= 27)
p2 = person(name='person2', address ='Mumbai', age=27)

p2.print_info()