# The custom exception class must be
# a derived class of exception
class InvalidAgeError(Exception):
    pass

def get_user_input():
    print("enter name: ")
    name = input()

    print("enter age: ")
    age = input()

    print(f"name = {name}")
    print(f"age = {age}")
get_user_input