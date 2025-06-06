
def  multiplication(p1,p2):
    multiplication = p1*p2
    return multiplication
answer = multiplication(40,60)
print(f"answer = {answer}")

def function4(p1,p2=40):
    print(f"inside function4")
    print(f"p1={p1}, type={type(p1)}")
    print(f"p1={p2}, type={type(p2)}")

function4(10)
function4(10,20)
function4(p1=20,p2=60)
function4(p1=1)