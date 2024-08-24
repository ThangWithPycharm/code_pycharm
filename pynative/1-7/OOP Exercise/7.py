""" OOP Bài 7: Kiểm tra loại đối tượng """
""" Viết chương trình để xác định xem đối tượng Bus đã cho thuộc về lớp nào """


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))
