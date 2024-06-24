""" Tính lập phương của tất cả các số từ 1 đến một số cho trước"""
""" Given:

input_number = 6

Expected output:

Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216
"""

input_number = int(input("Enter a number: "))
for i in range(input_number +1):
    print(f' current number is: {i} and the cube is {i**3}')