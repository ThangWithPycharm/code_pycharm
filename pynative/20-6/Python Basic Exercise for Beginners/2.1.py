"""Viết chương trình lặp 10 số đầu tiên, mỗi lần lặp in ra tổng của số hiện tại và số trước đó"""


for i in range(10):
    if i==0:
        previous_number=0
        sum=i+previous_number
    else:
        previous_number = i-1
        sum=i+previous_number

    print(f'current number is {i} previous number is {previous_number} sum = {sum}')



