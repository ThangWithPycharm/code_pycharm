""" Hiển thị chuỗi Fibonacci lên tới 10 số hạng """

""" Dãy số Fibonacci là một dãy số. Số tiếp theo được tìm bằng cách cộng hai số trước nó. Hai số đầu tiên là 0 và 1"""

num1 = 0
num2 = 1

for i in range(10):
    print(num1)
    result = num1 + num2
    num1 = num2
    num2 = result

