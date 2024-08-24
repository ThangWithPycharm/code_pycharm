""" Chọn xổ số ngẫu nhiên. Tạo 100 vé số ngẫu nhiên và chọn hai vé may mắn từ đó làm người chiến thắng. """
import random

numbers = random.sample(range(0, 1000), k=100)

choice = random.choices(numbers, k=2)
print(choice)
