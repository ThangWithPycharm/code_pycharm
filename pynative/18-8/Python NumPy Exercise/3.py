# Dưới đây là mảng numPy đã được cung cấp. Trả về mảng các
# phần tử bằng cách lấy cột thứ ba từ tất cả các hàng.
import numpy as np
sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

print(sampleArray[...,2])
print(sampleArray[:,2])