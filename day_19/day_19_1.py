def function1():
    # list mutable 
    numbers = [10, 20, 30 ,40, 50]
    countries = ["India", "USA", "UK"]
    
    numbers.append(60)
    countries.append("Japan")

    for number in numbers:
        print(number)
    
    print("-"*50)

    for country in countries:
        print(country)
function1()

def function2():
    # tuple (imputable)

    numbers = (10, 20, 30, 40, 50)
    countries = ("India", "USA", "UK")

    for number in numbers
        print(number)
    print("-"*50)

    for country in countries:
        print(country)
function2()