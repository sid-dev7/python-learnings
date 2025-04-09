class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi my name is {self.name} and my age is {self.age}")
# creating object of person 
person1 = person('Siddharth', 27)
person2 = person('Ananya', 25)
person1.introduce()
person2.introduce()
