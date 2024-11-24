# Vehicle management system 
# here we manage different vehicles (car, truck, etc.)
# TAP Goal pre-conditions post-conditions
# Based on Pillar - Inharitance

# Design
# Atrributes: - vehicle type, maker, model, color, year, engine status, cargo capacity.
# Methods: - Display info, Start/stop vehicle, disply cargo for truck
# classes: - vehicle (parent) , car/truck (child)
# Features 
    # 1. add multiple vahicles
    # 2. Show vahicles deatils
    # 3. Start or stop vahicles
    # 4. filter by vahicle type

# Parent class vahicle
class Vahicle:
    def __init__(self, maker, model, year, color):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
        self.engine_status = "Off"
    
    def start(self):
        if self.engine_status == "Off":
            self.engine_status = "On"
            print(f"{self.maker} {self.model} Started.")
        else:
            print(f"{self.maker} {self.model} is already running.")
            
    def stop(self):
        if self.engine_status == "On":
            self.engine_status = "Off"
            print(f"{self.maker} {self.model} Stopped.")
        else:
            print(f"{self.maker} {self.model} is already Off.")
            
    def displayInfo(self):
        print(f"{self.year} {self.color} {self.maker} {self.model}")


# inherit vahicle class 
class Car(Vahicle):
    def __init__(self, maker, model, year, color):
        super().__init__(maker, model, year, color)
    
class Truck(Vahicle):
    def __init__(self, maker, model, year, color, cargo_capacity):
        self.cargo_capacity = cargo_capacity 
        super().__init__(maker, model, year, color)
        
        
        
    def displayInfo(self):
        super().displayInfo()
        print(f"Cargo capacity {self.cargo_capacity} tons")
  
  
    
# object initiation
car1 = Car("Mahindra","Thar",2020, "Black" )
truck1 = Truck("TATA", "T-250", 2015, "White", 30)


# Start and Display
car1.start()
car1.displayInfo()

truck1.start()
truck1.displayInfo()

# Stop vahicles
car1.stop()
truck1.stop()


# Add two class MotorCycle and Bus
#  Enhance project adding - fuel level, and UI