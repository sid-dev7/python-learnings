def create_table(number):
    def inner (count = 10):
        table = [number * index for index in range (1, count+1)]
        print(table)
    return inner
number_2 = create_table(2)
number_2()