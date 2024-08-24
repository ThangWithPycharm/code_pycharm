""" Kiểm tra xem tất cả các mục trong bộ dữ liệu có giống nhau không """
def check(t):
    return any(i == t[0] for i in t)


tuple1 = (45, 45, 8, 45)
print(check(tuple1))


