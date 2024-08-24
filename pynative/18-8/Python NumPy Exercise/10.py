# Tạo hai mảng 2 chiều và vẽ chúng bằng matplotlib.

import numpy as np
import matplotlib.pyplot as plt
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1)


# Vẽ mảng đầu tiên
plt.subplot(1, 2, 1)  # Tạo một subplot với 1 hàng và 2 cột, và vẽ vào subplot đầu tiên
plt.imshow(arr_1, cmap='viridis')
plt.title('Array 1')
plt.colorbar()

plt.show()