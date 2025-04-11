# def divide (n1,n2):
#     #Try block
#     try:
#         # exception can be generated
#         division = n1/n2
#         print(f"division = {division}")
#     #except block
#     except:
#         print(f"exception has raised")

# divide(10,9)

def read_file():
    try:
        file = open("./myfile.txt", "r")
        data = file.read()
        print(f"data = {data}")
        file.close
    except:
        print(f"The file does not exist")
read_file()