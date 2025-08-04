def add(p1,p2):
    print("-"*40)
    print(f"inside the fucntion add")
    print(f"p1 ={p1}, p2={p2}")
    add = p1+p2
    print(f'addition= {add}')
    print("-"*40)
add(10,2)

# divide 
def divide(p1,p2):
    print("-"*40)
    print(f"inside the fucntion divide")
    print(f"p1 ={p1}, p2={p2}")
    division = p1/p2
    print(f' division= {division}')
    print("-"*40)
divide(10,1)


def log(function):
    print(f"function name = {function.__name__}")

log(add)
log(divide)