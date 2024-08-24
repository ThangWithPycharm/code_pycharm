""" OOP Exercise 6: Class Inheritance
OOP Bài tập 6: Kế thừa lớp """
""" 
Tạo một lớp con Bus kế thừa từ lớp Xe. Phí giá vé mặc định của bất kỳ phương tiện nào là sức chứa chỗ ngồi * 100. 
Nếu Xe là phiên bản Xe buýt, chúng tôi cần thêm 10% trên giá vé đầy đủ làm phí bảo trì. 
Vì vậy, tổng giá vé cho xe buýt sẽ trở thành số tiền cuối cùng = tổng giá vé + 10% tổng giá vé
 Lưu ý: Sức chứa chỗ ngồi của xe buýt là 50. vì vậy số tiền vé cuối cùng sẽ là 5500. 
 Bạn cần ghi đè phương thứcfare() của một lớp Xe trong lớp Xe buýt."""


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileague = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/100
        return amount


school_bus = Bus("school volvo ", 12, 50)
print("total  bus dare is ", school_bus.fare())
