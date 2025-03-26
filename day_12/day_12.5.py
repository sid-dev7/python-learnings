class person:
    """
    This class represents a person object..
    
    """
    def print_info(self):
        print(f"name:{self.name}")
        print(f"address: {self.address}")
        print(f"age: {self.age}")
    def can_vote(self):
        if self.age >= 18:
            print(f"{self.name} is eligible for vote")
        else:
            print(f"{self.name} in NOT eligible for vote")
p1 = person()
p1.name = "person1"
p1.age = 20
p1.address = "Pune"
p1.print_info()
p1.can_vote()
