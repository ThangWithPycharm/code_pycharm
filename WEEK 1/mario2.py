while True:
    try:
        height = int(input('height: '))
        if 0 < height < 9:
            break
    except ValueError:
        print("nhap so integer")

for i in range(1, height+1):
    # in khoang trang
    for j in range(0, height - i):
        print(" ", end="")
    # in vien gach
    for k in range(1, i+1):
        print("#", end="")
    # in 1 khaong trang
    for h in range(0,2):
        print(" ",end="")
    # in cac vien gach
    for l in range(1,i+1):
        print("#",end="")
    # in khoang trang khi xuong dong
    print()
