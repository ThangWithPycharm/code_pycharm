""" Tạo hàm bên trong để tính phép cộng theo cách sau """
""" 
Tạo một hàm bên ngoài sẽ chấp nhận hai tham số, a và b
Tạo một hàm bên trong bên trong một hàm bên ngoài sẽ tính toán phép cộng của a và b
Cuối cùng, một hàm bên ngoài sẽ cộng 5 vào phép cộng và trả về nó
"""


def outside(num1, num2):
    def inside(num1, num2):
        total = num1 + num2
        return total

    defo = inside(num1, num2)
    return defo + 5


a = outside(5, 5)
print(a)
