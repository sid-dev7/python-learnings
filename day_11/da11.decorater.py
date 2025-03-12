def log(function):
    def inner(p1, p2):
        print("_" * 40)
        print(f"inside function named = {function.__name__}")
        print(f" p1 = {p1}, p2 ={p2}")
        function(p1,p2)
        print("_" * 40)
    return inner
@log
def add(p1, p2):
    print(f"addition = {p1 +p2}")

add(10, 20)

#code2
@log
def divide(p1,p2):
    print(f"division = {p1/p2}")
divide(10,5)