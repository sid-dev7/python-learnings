#emty dictionary
# d1 ={}
# print(f"d1 = {d1}, type = {type(d1)}")

# def function2():
person1 = ("person1", "Pune", "person1.com")
person2 = ("person2", "Mumbai","person2.com")

print(f"name = {person1[0]}")
print(f" address = {person1[1]}")
print(f" email address = {person1[2]}")

print("-"*20)

print(f"name = {person2[0]}")
print(f" address = {person2[1]}")
print(f" email address = {person2[2]}")


# function2()








person = {
"name": "person1",
"age": 40
}
# name = "person1"
print(f"name: {person.get('name')}")
# phone = None
print(f"phone: {person.get('phone')}")
# the application crashes by sending an error (KeyError)
print(f"phone: {person['phone']}")