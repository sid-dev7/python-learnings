# logical operators

# and => &&
# True and True => True
# True and False => False
# False and False => False
# False and False => False

age = 100
#  age >20 and age < 60
if (age > 20) and (age<60):
    print(f"inside if block")
    print(f"age valid for employee")
else:
    print(f"inside if block")
    print("age not valid for employee")

# or => //
# and => &&
# True or True => True
# True or False => True
# False or False => True
# False or False => False

#  age >20 or age < 60
if (age > 20) or (age<60):
    print(f"inside if block")
    print(f"age valid for employee")
else:
    print(f"inside if block")
    print("age not valid for employee")