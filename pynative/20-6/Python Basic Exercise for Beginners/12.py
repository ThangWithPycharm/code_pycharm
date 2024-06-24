""" Tính thuế thu nhập cho thu nhập nhất định bằng cách tuân thủ các quy tắc dưới đây """
""" First $10,000	0
    Next $10,000	10
    The remaining	2 """
""" Ví dụ: giả sử thu nhập chịu thuế là 45000 và thuế thu nhập phải nộp là
10000*0% + 10000*10%  + 25000*20% = 6000 USD """


def fee_tax(fee):
    if fee > 10000:
        tax_payable = 10000 * (0 / 100) + 10000 * (10 / 100) + (fee - 20000) * (20 / 100)
        print(f'tax_payable = {tax_payable}')
    else:
        print(f'tax_payable = 0')


fee_tax(100000)
