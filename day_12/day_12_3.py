class person:
    pass
p1 = person()
setattr(p1, "name", "address")
setattr(p1, "age", 30)

print(f"name: {getattr(p1, 'name')}")
print(f"age: {getattr(p1, 'age')}")

p2 = person()
setattr(p2, "name", "person2")
setattr(p2, "age", 10)

print(f"name: {getattr(p1, 'name')}")
print(f"age: {getattr(p2, 'age')}") 

