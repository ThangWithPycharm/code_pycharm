""" Viết tất cả nội dung của một tệp đã cho vào một tệp mới bằng cách bỏ qua dòng số 5 """

# mo file
with open("F:/pycharm/test.txt", "r") as f:
    lines = f.readlines()
    print(lines)

with open("F:/pycharm/test_new.txt", "w") as f:
    count = 0
    for line in lines:
        count += 1
        if count == 5:
            pass
        else:
            f.write(line)
    print(f)