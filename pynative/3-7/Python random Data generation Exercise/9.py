""" Đổ xúc xắc sao cho lần nào bạn cũng nhận được số giống nhau """
""" Xúc xắc có 6 số (từ 1 đến 6). Đổ xúc xắc sao cho lần nào bạn cũng phải nhận được cùng một số đầu ra. 
làm điều này 5 lần """

import random

dice = [1,2,3,4,5,6]
print(" random number with seed 30")
for i in range(5):
    random.seed(20)
    print(random.choice(dice))
