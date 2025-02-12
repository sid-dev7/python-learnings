# def function_1():
#     numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#     numbers_slice = []
#     positions = [2, 3, 4, 5]
#     for index in positions:
#         numbers_slice.append(numbers[index])
#     print(numbers_slice)

# function_1()

def function_2():
     
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    #slicing (2, 3, 4, 5)
    print(numbers[2:6])
    # numbers[0:5] = [10, 20, 30, 40, 50]
    print(f"numbers[0:5] = {numbers[0:5]}")
    # numbers[:5] = [10, 20, 30, 40, 50]
    print(f"numbers[:5] = {numbers[:5]}")
    # numbers[6:10] = [70, 80, 90, 100]
    print(f"numbers[6:10] = {numbers[6:10]}")
    # numbers[6:] = [70, 80, 90, 100]
    print(f"numbers[6:] = {numbers[6:]}")

    # numbers[:] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # numbers[0:10]
    print(f"numbers[:] = {numbers[:]}")
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # numbers[0:9:2] = [10, 30, 50, 70, 90]
    print(f"numbers[0:9:2] = {numbers[0:9:2]}")
    # numbers[1:9:2] = [20, 40, 60, 80]
    print(f"numbers[1:9:2] = {numbers[1:9:2]}")
    # numbers[::] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"numbers[::] = {numbers[::]}")
    # numbers[::] = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    print(f"numbers[::] = {numbers[::-1]}")
function_2()