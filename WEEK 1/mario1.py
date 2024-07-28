while True:
    try:
        height = int(input("what height do you want? "))
        if 1 < height < 9 :
            break
    except ValueError:
        print(" vui long nhap integer")

# in so dong mong muon
for i in range(0,height):
    # in khoang trang
    for j in range(1,height-i):
        print(" ",end="")
    # in cac vien gach
    for k in range(0,i+1):
        print("#",end="")
    print()
