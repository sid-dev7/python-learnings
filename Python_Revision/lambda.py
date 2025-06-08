def square(number):
    return number**2
# inline function (lambda function)
print(f"square of 9 = {square(9)}")
# labmda function
cube = lambda number: number **3
print(f"cube of 9 = {cube(9)}")
print(f"cube = {cube}")
print(f"type cube = {type(cube)}")

def add(p1,p2):
    return p1+p2 
# myAdd = add
addition = add(30,40)
print(f" addition of 30 + 40 = {addition}")

lambda_add = lambda p1,p2: p1 + p2

print(f"addtion of 10, 20= {lambda_add(10,20)}")