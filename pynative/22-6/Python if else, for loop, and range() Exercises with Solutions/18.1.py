""" In ra các hàng tăng dần từ 1 đến 5 sao.
In ra các hàng giảm dần từ 4 đến 1 sao.
"""

for i in range(1, 6):
    for j in range(i):
        print('*', end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print('*', end=" ")
    print()