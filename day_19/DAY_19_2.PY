import numpy as np

# def function1():
#     # python list
#     list1 = [10, 20, 30, 40, 50]
#     print(f"list  ={list1}, type= {type(list1)}")

#     #numpy array
#     a1 = np.array([10, 20, 30, 40, 50])
        
#     print(f"a1 = {a1}, type = {type(a1)}")
#     print(f" item size = {a1.itemsize}")
#     print(f"dataype ={a1.dtype}")
#     print(f" total memory = {a1.itemsize*a1.size}")
# function1()

print("-"*80)
def function3():
    a3 = np.array(
        [
            [10, 20, 30, 40, 50],
            [60, 70, 80, 90, 100]
        ], dtype=np.int16)
    print(f"a3 = {a3}, type = {type(a3)}")
    print(f"item size = {a3.itemsize}")
    print(f"dataype = {a3.dtype}")
    print(f"total memory = {a3.itemsize*a3.size}")
    print(f"total memmory = {a3.nbytes}")
    print(f"total memmory = {a3.shape}")
    print(f"total memmory = {a3.ndim}")
function3()