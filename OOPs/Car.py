class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def displyInfo(self):
        print(f"Car Info: {self.year} {self.make} {self.year}")
        
        
my_car = Car("Mahindra", "Thar", 2020)
your_car = Car("TATA", "Nano", 2010)
print(f"My car is {my_car.displyInfo()}")
print(f"Your car is {your_car.displyInfo()}")