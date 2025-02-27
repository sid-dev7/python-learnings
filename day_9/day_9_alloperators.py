def add(p1, p2):
    print(f"addition = {p1+p2}")


def subtract(p1,p2):
    print(f"subtraction = {p1-p2}")

def multiplication(p1,p2):
    print(f" mutliplicaiton = {p1*p2}")
def division(p1, p2):
    print(f"division= {p1/p2}")

def execute(function):
    # function = add
    print(f"function = {function}")
    function(10,20)
    function(20,20)
    function(100,40)

execute(add)
execute(subtract)
execute(multiplication)
execute(division)



# (10,20)
# (20,40)
