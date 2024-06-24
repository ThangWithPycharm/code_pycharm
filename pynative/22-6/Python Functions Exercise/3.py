""" Bài tập 3: Trả về nhiều giá trị từ một hàm """

""" Viết chương trình tạo hàm tính toán() sao cho nó có thể nhận hai biến và tính toán phép cộng và phép trừ. 
Ngoài ra, nó phải trả về cả phép cộng và phép trừ trong một lệnh gọi return """


def calculate(num1, num2):
    tong = num1 + num2
    hieu = num1 - num2
    return tong, hieu


result = calculate(1, 2)
print(f" tong = {result[0]} hieu = {result[1]}")
