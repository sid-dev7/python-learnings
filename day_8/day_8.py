def get_square(number):
    return number**2
def function5():
    numbers = [1,2,3,4,5,6]
    squares = list(map(get_square, numbers))
    print(numbers)
    print(squares)
function5()
