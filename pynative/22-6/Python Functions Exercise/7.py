""" Gán một tên khác cho function và gọi nó bằng tên mới """
""" Dưới đây là hàm display_student(tên, tuổi). Gán một tên mới show_tudent(name, age) cho nó và gọi nó bằng tên mới 
Given:


def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
You should be able to call the same function using

show_student(name, age)


"""

def display_student(name, age):
    print(name, age)

display_student('thang', 25)
show_student = display_student
show_student("Emma", 26)
