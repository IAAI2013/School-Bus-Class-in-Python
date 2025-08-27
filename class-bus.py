class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

obj = Bus("Superbus DB", 250, 132)
print("School Bus Details: ")
print("Name: ", obj.name)
print("Maximum Speed: ", obj.max_speed)
print("Mileage: ", obj.mileage)