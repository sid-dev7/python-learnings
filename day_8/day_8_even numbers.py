def function1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in numbers:
        if number   %2 == 0:
            print(number)
function1()

#  get even number by lambda
def function2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers =[]
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(number)
    print(even_numbers)
function1()



# map and filter
def function3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_numbers = list(map(lambda x : x % 2 == 0, numbers))
    even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(number)
    print(even_numbers)
function3()

def function4():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 10},
        {"model": "i00", "company": "hyundai", "price": 15.5},
        {"model": "nano","company": "tata", "price": 16.5},
        {"model": "i20", "company": "hyundai", "price": 09.0},
    ]
#price < 10

    affordable_cars = list(filter(lambda car: car['price'] < 10, cars))
    print(cars)
    print(affordable_cars)
function4()
