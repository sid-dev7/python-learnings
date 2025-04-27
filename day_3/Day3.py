
#Or Rules=>
    #true or true => true
    #true or false => true
    #false or true => true
    #false or false => false

#And Rules=>

    #true and true => true
    #true and false => false
    #false and true => false
    #false and false => fals

# code 1

#age = 34
#if age > 20:
 #print("age is greater than 20")
#else:
 #print("age is less than 20")
#print ("this out of if and else block")

#Code 2

# age = 34
# if (age > 25) and (age <60) and (age <25):
#     print(f"{age} is within the limit")
# else:
#     print(f"{age} is not within the limit")


#Code 3 Or operator
# age = 61

# if (age > 25) or (age <60):
#  print(f"{age} is within the limit")
# else:
#  print(f"{age} is not within the limit")

 #Code 4 If Else operator voter age

#age = 61

#if (age>=18 ):
 #print(" Person eligible for voting")
#else:
 #print("Person not eligible for voting")


#Code 5 Def Functions

# defining paramiterized function

# def function1():
#     print("This is a function body")
# # calling a function
# function1()
# v1 = "sid"
# v2 = 10
# def function2(K): #K can be anything like Param/G/J
#     print(f"param ={K}, type = {type(K)}")

# function2("Sid")   #Str
# function2(10)      #int
# function2(10.56)   #Float
# function2(True)    #boolean 

# code 6 Adding to parameters

# def add(P1, P2):

#     addition = P1 + P2
#  print(f"Addtion = {addition}")

# add(10,40)
# add(10.5,40.67)

# add("Hello","Sid")
# add(True,False)

#code 7 

def add(P1, P2):
    """ this function will add parameter.

    :param p1: integer, first argument 
    :param p2: integer, second argumnet
    :return: nothing
    """
    print("inside the function")
    addition = P1 + P2
    print(f"addition = {addition}")

# dunder doc->(.__doc__), prints data in """" --"""" is caled docstring

print(add.__doc__) 
  
# add(10, 40)


#Code 8 

# def function_3(num1, num2, num3):
#  print(f"num1 = {num1}, num2 = {num2}, num3 = {num3}")
# function_3(10, 30, 40)
