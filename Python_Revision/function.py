# function
# defining a function
def function1():
    print(f"inside function1")
    print(f"this is function body")
# function call
function1()

# parameterized function
def function2(param):
    print("inside function2")
    print(f"param = {param}, type = {type(param)}")
function2("hello")

def add(p1,p2):
    print('inside add function')
    addition = p1+p2
    print(f"addition = {addition}")
add(10,30)