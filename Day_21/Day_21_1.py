import pandas as pd
import numpy as np

# def function1():
#     # one dementional array
#     s1 = pd.Series([10,20,30,40,50])
#     print(f" s1= {s1}, type = {type(s1)}")
# function1()

# # filtering
# def function2():
#     # one dementional array
#     s1 = pd.Series([10,20,30,40,50])
#     # +ve indexing
#     print(f"value at 0 = {s1[0]}")
#     print(f"value at 4 = {s1[4]}")
#     print(f"index = {s1.index}") #-ve indexing not supported
#     print(f"s1 > 30 = {s1 >30}")
#     # slicing
#     print(f"sq[:3] = {s1[:3]}")
#     print(f"sq[1:3] = {s1[1:3]}")
#     print(f"sq[2:] = {s1[2:]}")
# function2()

def function3():
    s1 = pd.Series({"model": "i20", "company":"Hyundai", "price": 7.5})
    print(s1)
    print(f"price = {s1['price']}")
    print(f"model = {s1['model']}")
    print(f"company = {s1['company']}")
function3()
