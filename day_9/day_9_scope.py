# scope: global
num = 100
print("befor calling function1 num = {num}")

def function1():
    print(f"inside function1")
    global num

    #modify gloabal num's value
    
    num = 500
    print(f"num = {num}")
function1()

# num = 500
print(f"after calling function1 num = {num}")


