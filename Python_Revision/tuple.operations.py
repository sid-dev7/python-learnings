# imuateble cant modify after defyning 
numbers_tuple = (10,20,30,40,50)
print(f"numbers = {numbers_tuple}, type={type(numbers_tuple)}")

print("-*-"*20)
# emty tuple

tuple_1 = ()

print(f"emty tuple = {tuple_1}, type = {type(tuple_1)}")
# if you do not put commma after any value it would not consider as tuple 
tuple_2 = (10,)

print(f"emty tuple = {tuple_2}, type = {type(tuple_2)}")

def math_operations(p1,p2):

    add = p1 +p2
    sub = p1-p2
    multi = p1*p2
    div= p1/p2
    return add, sub,multi,div
result = math_operations(10,2)
print(result)