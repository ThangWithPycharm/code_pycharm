#In tối đa từ trục 0 và tối thiểu từ trục 1 từ mảng 2-D sau.
import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print("printing amin of row axis 1\n",np.amin(sampleArray,1))
print("printing amax of colums axis 0\n",np.amax(sampleArray,0))
