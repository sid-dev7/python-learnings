def add(p1, p2):
    return f"{p1} + {p1} = {p1 +p2}"
def subtract(p1, p2):
    return f"{p1} - {p2} = {p1 -p2}"

def execute(function):
    print('-'* 40)
    print(function(20,10))
    print('-'* 40)
execute (add)
execute(subtract)