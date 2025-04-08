class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
    def print_person_info(self):
        print(f"name = {self.name}")
        print(f"address = {self.address}")
        print(f"age = {self.age}")
class Player(Person):
    def __init__(self, name, address, age, team):
        Person.__init__(self,name, address, age)
        self.team = team
    def print_player_info(self):
         print(f"name = {self.name}")
         print(f"address = {self.address}")
         print(f"age = {self.age}")
         print(f"team ={self.team}")

#base class object
person1 = Person('person', 'Pune', 10)
person1.print_person_info()

#derived class object
Player1 = Player('player1','Mumbai',20,'india')
Player1.print_person_info()
