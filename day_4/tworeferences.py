#int dedfine values

# num = 100

# print(f"num = {num}, type = {type(num)}")

# num2= num

# num = 300

# print(f"num = {num}, type = {type(num)}")
# print(f"num2= {num2},type = {type(num2)}")

# function having same reference 

def function1():
    print("inside function")
print(f"function1, = {function1}")
print(f"function1 type = {type(function1)}")

myfunction = function1
print(f"myfunction = {myfunction}")

print(f"myfunction = {myfunction}")

print(f"myfunction type ={type(myfunction)}")
