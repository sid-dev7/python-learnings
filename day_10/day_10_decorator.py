def execute(function):
    print("inside function")
    print("function = {function}, type = {type(function)}")
    def inner(p1, p2):
        print("-"*50)
        print(function(p1, p2))
        print("-"*50)
    return inner

@execute
def add(p1,p2):
    return f"{p1} + {p2} = {p1 + p2}"
@execute
def subtract(p1, p2):
    return f"{p1} - {p2} = {p1 - p2}"
@execute
def  multiply(p1, p2):
    return f"{p1} * {p2} = {p1 * p2}"

add(10, 20)
subtract(10, 20)
multiply(10, 40)

#code:2
def decorate_result(function):
    def inner(p1, p2):
        print("*" * 40)
        function(p1, p2)
        print("*" * 40)
    return inner
@decorate_result
def  add(p1, p2):
    print(f"add = {p1 + p2}")
@decorate_result
def subtraction(p1, p2):
    print(f"subtraction = {p1 - p2}")

add(50, 30)
subtraction(50,50)