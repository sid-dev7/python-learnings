# def function1():
    # single dimentional
    # list1 = [10, 20, 30, 40, 50]
#     print(f"{list1}")
#  # list of list 
#  #multi dimentional 
#     # list2 = [
#     #     [10, 20],
#     #     [30, 40],
#     #     [50, 60]
#     ]
#     print(f"list2[0], {list2[0]}")
#     print(f"list2[0], {list2[0][0]}")
#     print(f"list2[0], {list2[0][1]}")
# function1()


def function3():
    # List of dictionaries
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 10},
        {"model": "Nano", "company": "TATA", "price": 40},
    ]  
    for car in cars:
        print(f"Model: {car['model']}")
        print(f"Company: {car['company']}")
        print(f"Price: {car['price']}")
        print('-' * 20)

# Call the function
function3()

#learned about terminal commands and imporatance of running code from terminals
