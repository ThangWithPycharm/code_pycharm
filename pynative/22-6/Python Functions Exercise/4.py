""" Tạo một hàm với đối số mặc định """
""" Viết chương trình tạo hàm show_employee() sử dụng các điều kiện sau.
Nó phải chấp nhận tên và lương của nhân viên và hiển thị cả hai.
Nếu thiếu lương trong lệnh gọi hàm thì gán giá trị mặc định 9000 cho lương """


def show_employee(name, salary=9000):
    print(" salary of ", name, "is", salary)


show_employee('thang', 2000)
show_employee('thang')
