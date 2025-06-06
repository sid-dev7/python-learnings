class person:
    """
    This class represents a person object..
    
    """
    def __init__(self):

        """
        initializer method
        - gets calledautomatically for every object of this class
        - similar to constructor
        """
        print("inside __init__")
        self.name = ""
        self.address = ""
        self.age = 0

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
# initializer method
# removed change


# initializer (constructor)
# de-initializer (destructor)
# setter (mutator)
# getter (inspector)
# facilitator (utility)

