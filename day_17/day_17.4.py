# The custom exception class must be
# a derived class of exception
class InvalidAgeError(Exception):
    pass

def get_user_input():
    print("enter name: ")
    name = input()

    print("enter age: ")
    age = input()
    #convert the string to int
    age = int(age)
    if (age < 0) or (age > 100):
        #raise an exception
        raise IndentationError()
    print(f"name = {name}")
    print(f"age = {age}")
get_user_input()