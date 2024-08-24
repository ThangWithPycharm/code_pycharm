#  Xóa cột thứ hai khỏi một mảng nhất định và
#  chèn cột mới sau vào vị trí của nó.
import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
newColumn = np.array([[10, 10, 10]])

print(sampleArray)
array_new = np.delete(sampleArray, 1, axis=1)
print(array_new)

array_add = np.insert(array_new, 1, newColumn, axis= 1)
print(array_add)