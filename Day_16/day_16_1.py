class Vehicle:
    def __init__(self, model, company, price):
        self._model = model
        self._price = price
        self._company = company

    def print_info(self):
        pass
class Bike(Vehicle):
    def __init__(self, model, company, price):
        Vehicle.__init__(self, model, company, price)
    def print_info(self):
        print(f"--Bike Information--")
        print(f"model = {self._model}")
        print(f"company = {self._company}")
        print(f"price = {self._price}")
class Car(Vehicle):
    def __init__(self, model, company, price, fuel_type):
        Vehicle.__init__(self, model, company, price)
        self._fuel_type = fuel_type
    def print_info(self):
        print(f"--Car Information--")
        print(f"model: {self._model}")
        print(f"company: {self._company}")
        print(f" price = {self._price}")
        print(f"fuel type = {self._fuel_type}")

b1 = Bike('activa','honda',75000)
b1.print_info()
c1 = Car('i20','hyudai',750000,'petrol')
c1.print_info()
