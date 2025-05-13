import pandas as pd
import numpy as np

def function1():
    # one dementional array
    s1 = pd.Series([10,20,30,40,50])
    print(f" s1= {s1}, type = {type(s1)}")
function1()

# filtering
def function2():
    # one dementional array
    s1 = pd.Series([10,20,30,40,50])
    # +ve indexing
    print(f"value at 0 = {s1[0]}")
    print(f"value at 4 = {s1[4]}")
function2()