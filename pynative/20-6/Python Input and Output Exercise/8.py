""" Định dạng biến bằng phương thức string.format() """
""" Viết chương trình sử dụng phương thức string.format() để định dạng ba biến sau theo kết quả mong đợi

totalMoney = 1000
quantity = 3
price = 450
I have 1000 dollars so I can buy 3 football for 450.00 dollars."""

print(" i have {totalMoney} so i can buy {quantity} football for {price: .2f} dollars. ".format(totalMoney=10000,
                                                                                                quantity=3, price=450))
