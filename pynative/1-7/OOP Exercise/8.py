""" Bài tập OOP 8: Xác định xem School_bus có phải là một thực thể của lớp Vehicle không """


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))
