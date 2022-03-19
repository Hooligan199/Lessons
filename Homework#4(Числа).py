import sys

a = int(input("Число:"))

if 99 >= a <= 999 or a == -a:
    print("Только трехзначные положительные числа")
    sys.exit()

print(str(a)[::-1])
