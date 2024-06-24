""" Calculate the sum of all numbers from 1 to a given number"""
""" Expected Output:
    Enter number 10
    Sum is:  55 """

sum = int(input("Enter number: "))
total = 0
for i in range(1, sum+1):
    total = total + i
print('+'.join(str(i) for i in range(1, sum + 1)))
print('sum is ',total)

