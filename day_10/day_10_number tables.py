def create_table(number):
    def inner (count = 10):
        # table = [number * index for index in range (1, count+1)]
        # print(table)
        for index in range(1, count+1):
            print(f"{number} * {index} = {number * index}")
    return inner
number_2 = create_table(2)
number_2(20)