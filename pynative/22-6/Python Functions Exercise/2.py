""" Tạo một hàm có độ dài đối số thay đổi"""
""" # call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)
Expected Output:

Printing values
20
40
60


Printing values
80
100"""

def func1(*args):
    print(args)

func1(20, 40)
