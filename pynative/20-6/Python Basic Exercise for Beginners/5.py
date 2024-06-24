'''Kiểm tra xem số đầu tiên và số cuối cùng của danh sách có giống nhau không '''
'''Viết một hàm để trả về nếu số đầu tiên và số cuối 
cùng của một danh sách đã cho giống nhau. Nếu số khác nhau thì trả về'''

def check_similar(numbers):
        if numbers[0]==numbers[-1]:
            print('result is True')
        else:
            print('result is False')

numbers=[10,20,30]
print('given list:',numbers)
check_similar(numbers)

