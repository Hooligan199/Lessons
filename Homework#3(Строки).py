c = "замена в строке"
b = input("Введите что-нибудь:")
a = "Это строка в которую {} новую строку"
print(a.format(b))
print(a.format(c))
print(len(a))
if "строка" in a:
    print("Yes")
else:
    print("No")
