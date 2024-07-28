while True:
    try:
        cents = int(input("change owed: "))
        if cents >= 0:
            break
    except ValueError:
        print("vui lòng nhập số nguyên!")

quarters = 0
while cents >= 25:
    cents = cents - 25
    quarters += 1

dimes = 0
while cents >= 10:
    cents = cents - 10
    dimes += 1

nickels = 0
while cents >= 5:
    cents = cents - 5
    nickels += 1

pennies = 0
while cents > 0:
    cents = cents - 1
    pennies += 1

sum = quarters + dimes + nickels + pennies
print(sum)
