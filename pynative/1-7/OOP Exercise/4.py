""" Class Inheritance """
""" Create a Bus class that inherits from the Vehicle class. 
Give the capacity argument of Bus.seating_capacity() a default value of 50 """


class Vehicle:
    def __init__(self, name, max_speed, mileague):
        self.name = name
        self.max_speedd = max_speed
        self.mileague = mileague

    def seating_capacity(self, capacity):
        return f"the seating capacity of a {self.name} is {capacity} passenger"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


bus = Bus("school volco", 120, 14)
print(bus.seating_capacity())
