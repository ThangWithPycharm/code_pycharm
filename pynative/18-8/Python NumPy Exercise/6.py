# Tạo một mảng số nguyên 8X3 từ một phạm vi từ 10 đến 34 sao cho chênh lệch giữa
# mỗi phần tử là 1 sau đó Chia mảng thành bốn mảng con có kích thước bằng nhau

import numpy as np
arr_1 = np.arange(10,34)
arr_1 = arr_1.reshape(8,3)
print(arr_1)
split_arr = np.split(arr_1,4)
print(split_arr)
