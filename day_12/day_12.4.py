class car:
    # method
    def print_info(self):
        print(f"model = {self.model}")
        print(F"Company = {self.company}")
c1 = car()

print(car.__dict__)

#adding attributes
c1.model = "i20"
c1.company =  "Hyundai"

c1.print_info()
c2 = car()
c2.model = "Nexon"
c2.company = "TATA"
#car.print_info gets caled iwth c2 value
c2.print_info()
# c1.print_info = print_info

# c1.print_info(c1)



