c = "замена в строке"
b = input("Введите что-нибудь:")
a = "Это строка в которую {} новую строку"
print(a.format(b))
a = a.format(c)
print(a)
print(len(a))
if "строка" in a:
    print("Yes")
else:
    print("No")
