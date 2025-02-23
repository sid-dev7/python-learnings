# map function

# def get_square(number):
#     return number**2
# def function5():
#     numbers = [1,2,3,4,5,6]
#     squares = list(map(get_square, numbers))
#     squares = tuple(map(get_square, numbers))
#     print(numbers)
#     print(squares)
# function5()

def function6():
    tempC = [10, 20, 45, 60, 70, 100]
    TempF = tuple(map(lambda x: (x * (9/5) + 32), tempC))
    print(tempC)
    print(TempF)
function6()


