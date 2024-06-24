'''Trả về tích của hai số nguyên chỉ nếu tích đó bằng hoặc nhỏ hơn 1000.
Nếu không, trả về tổng của chúng'''

def sum_multi(a, b):
    if a*b<1000:
        print('the result is ',a*b)
    else:
        print('the result is ',a+b)


a = int(input('please enter number1 = '))
b = int(input('please enter number2 = '))
sum_multi(a,b)