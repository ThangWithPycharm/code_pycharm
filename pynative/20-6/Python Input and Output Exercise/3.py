""" Chuyển đổi số thập phân thành số bát phân bằng định dạng đầu ra print() """
""" Expected Output:
The octal number of decimal number 8 is 10 """

thap_phan = int(input(' nhap so: '))
print(f" The octal number of decimal number {thap_phan} is ", format(thap_phan, 'o'))