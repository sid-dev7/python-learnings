# def add(p1, p2):
#     addtion = p1 + p2
#     print(f"addition = {addtion}")

# add(10, 20)

# def divide(p1, p2):
#     print("✔"*50)
#     print("inside the function divide")
#     print(f"p1 = {p1}, p2 ={p2}")
#     division = p1 / p2
#     print(f"division = {division}")
#     print("✔"*50)
# divide (20,1)


# def log(function):
#     print(f"function name = {function.__name__}")
# log(add)
# log(divide)

#code3 use of args and kwargs 
def log(function):
    def inner(*args, **kwargs):
        print("✔"*50)
        print(f" inside function named = {function.__name__}")
        print(f"args ={args}")
        print(f"kwargs = {kwargs}")

        function(*args, **kwargs)
        print("✔"*50)

    return inner

@log
def add(p1, p2):
    print(f"addition = {p1+p2}")
add(10,20)
    
 