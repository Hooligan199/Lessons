import sys

first_number = int(input("Число:"))
revers_number = 0

if 99 >= first_number <= 999 or first_number == -first_number:
    print("Только трехзначные положительные числа")
    sys.exit()

while first_number != 0:
    digit = first_number % 10
    revers_number = revers_number * 10 + digit
    first_number //= 10

print(revers_number)
