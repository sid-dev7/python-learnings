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

def add(p1,p2):
    """
    this function add two parameter
    :param p1: integer first argument
    :param p2: integer second parameter
    :return: nothing
    """
    print('inside add function')
    addition = p1+p2
    print(f"addition = {addition}")
print(add.__doc__)
add("hey","hello")


def function3():
    """
    Documentation string (docstring)
    this is a test function
    """
    print("This is inside function3")
# print(function3.__doc__)