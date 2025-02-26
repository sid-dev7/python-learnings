# scope: global
num = 100
print(f"outside of any function num = {num}")
def function1():
    print("inside function1")
    print(f"num = {num}")
    
    # scope: local
    first_name = "steve"
    print(f"first name = {first_name}")
function1()