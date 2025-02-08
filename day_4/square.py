# def square(number):
#     return number**3
# print(f"square of 9 = {square(9)}")

#lambda function

# def cube(number):
#   return number ** 3
# 
# cube = lambda number: number ** 3
# print(f" cube of number is = {cube(9)}")

#function alias

def add(p1,p2):
    return p1+p2

myAdd = add

addition = add(30,40)
print(f"addtion of 30 and 40 = {addition}")

# lambda_add = lambda p1, p2: (p1+p2)
# print(f"lambda add = {lambda_add(10,20)}")