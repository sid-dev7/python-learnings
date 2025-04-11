def divide (n1,n2):
        # exception can be generated
        division = n1/n2
        print(f"division = {division}")

def read_file():
    file = open("./myfile.txt", "r")
    data = file.read()
    print(f"data = {data}")
    file.close()
 #Try block
try:
     divide(10,5)
     read_file()
#except block
#handles the exception raised in divide funtion
#specific except block
except ZeroDivisionError:
    print(f"zero division exception raised")

#specific except block
except FileNotFoundError:
      print(f" file not found exception")
#generic except block
except:
      print("generic exception raised")