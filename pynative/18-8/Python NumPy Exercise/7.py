# Sắp xếp theo mảng NumPy
#Trường hợp 1: Sắp xếp mảng theo hàng thứ 2
#Trường hợp 2: Sắp xếp mảng theo cột thứ 2

import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print("original array\n", sampleArray)

rows = sampleArray[:,sampleArray[1,:].argsort()]
clumns = sampleArray[sampleArray[:,1].argsort()]

print(rows)
print(clumns)