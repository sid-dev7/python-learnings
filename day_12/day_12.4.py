class car:
    pass

def print_info(car):
    print(f"model = {car.model}")
    print(F"Company = {car.company}")
c1 = car()

#adding attributes
c1.model = "i20"
c1.company =  "Hyundai"
c1.print_info = print_info

c1.print_info(c1)
