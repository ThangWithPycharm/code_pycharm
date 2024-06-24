"""Viết chương trình lặp 10 số đầu tiên, mỗi lần lặp in ra tổng của số hiện tại và số trước đó"""


for i in range(10):
    a=i
    b=i-1
    sum=a+b
    if i==0:
        print(f'so hien tai la {i}, so truoc do la {i}, sum: {i}')
    else:
        print(f'so hien tai la {i}, so truoc do la {i-1}, sum: {sum}')




