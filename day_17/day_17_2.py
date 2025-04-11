def divide (n1,n2):
        # exception can be generated
        division = n1/n2
        print(f"division = {division}")

        print(f"exception has raised")
 #Try block
try:
     divide(10,2)
    #except block
except:
    print(f"Error raised")