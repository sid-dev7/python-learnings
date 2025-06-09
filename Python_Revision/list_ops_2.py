def  function1():
    numbers=[10,20,30,40,50]
    
    numbers.append(60)
    print(numbers)

    numbers.insert(3,70)
    print(numbers)

    numbers.pop()
    print(numbers)

    numbers.pop(2)
    print(numbers)

    numbers.remove(20)
    print(numbers)
function1()


def  function2():
    numbers=[10,20,30,40,50]
    # +ve indexing
    print(f"value at first position = {numbers[0]}")
    # -ve indexting
    print(f"value at last position = {numbers[-1]}")
function2()

# slicing 
def  function3():
    numbers=[10,20,30,40,50]

    numbers_slice = []
    positions = [0,3,4]

    for index in positions:
        numbers_slice.append(numbers[index])
    print(numbers_slice)
function3()