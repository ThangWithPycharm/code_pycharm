import os

file_path = "F:/pycharm/test.txt"

# Tạo hoặc xóa nội dung của file để nó trống
with open(file_path, 'w') as file:
    txt='thangducccc'
    file.truncate()

# Kiểm tra lại kích thước file
size = os.stat(file_path).st_size

if size == 0:
    print('file is empty')
else:
    print('file size: %d' % size)
