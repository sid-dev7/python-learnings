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

def function2():
    # list of lists
    list1 = [
        [10, 20],
        [30, 40, 50]
        [60, 70, 80, 90, 100]
    ]

    for row in list1:
        for col in row:
            print(f"value = {col}")
    print(f"-" * 10)
function2()    



