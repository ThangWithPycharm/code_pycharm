""" Tạo một lớp con Bus sẽ kế thừa tất cả các biến và phương thức của lớp Xe
Expected Output:

Vehicle Name: School Volvo Speed: 180 Mileage: 12 """


class Vehicle:
    def __init__(self, name, max_speed, mileague):
        self.name = name
        self.max_speed = max_speed
        self.mileague = mileague


class Bus(Vehicle):
    def display(self):
        print(f"Vehicle name: {self.name} speed: {self.max_speed} Mileague:{self.mileague}")


bus = Bus("School Volvo", 180, 12)
bus.display()
