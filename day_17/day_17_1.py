def divide (n1,n2):
    #Try block
    try:
        # exception can be generated
        division =n1/n2
        print(f"division = {division}")
    except:
        print(f"exception has raised")

divide(10,0)