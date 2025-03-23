#empty class
class person:
    pass
#instantiation: creating an object of class
# reference = object 
# object is collection of key value pairs
person = person()
print(person)
print(person.__dict__)

# add new key

setattr(person, "name", "person1")
setattr(person, "address", "pune")
setattr(person,"age", 27)

# print(person.__dict__)

#get value of attribute name

print(f"name = {getattr(person, 'name')}")
print(f"address = {getattr(person,'address')}")
print(f"age = {getattr(person,'age')}")

