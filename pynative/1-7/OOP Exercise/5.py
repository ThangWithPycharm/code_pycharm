""" Xác định thuộc tính lớp “color” với giá trị mặc định là màu trắng.
Tức là mọi phương tiện đều phải có màu trắng
Expected Output:Đầu ra dự kiến:

Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
"""


class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


bus = Bus("school volvo", 180, 12)
car = Car("Audi Q5", 240, 18)
print(f"color: {bus.color} Vehocle name: {bus.name} speed: {bus.max_speed} Mileage: {bus.mileage}")
print(f"color: {car.color} Vehocle name: {car.name} speed: {car.max_speed} Mileage: {car.mileage}")
