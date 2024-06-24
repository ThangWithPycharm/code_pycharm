""" Viết hàm có tên exexpon(base, exp) trả về giá trị int của cơ số lũy thừa của exp """
""" Ghi chú ở đây exp là một số nguyên không âm, và cơ số là một số nguyên """
""" example 
base = 5
exponent = 4

5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625) """


def exexpon(base, exp):
    base = int(base)
    exp = int(exp)

    # tinh luy thua
    result = base ** exp

    if exp == 0 :
        calculation = 1
    else:
        calculation = " * ".join([str(base)] * exp)
    print(f' {base}^{exp} = {result} ')
    print(f'i.e. {calculation} = {result}')
    return result


exexpon(2, 5)
