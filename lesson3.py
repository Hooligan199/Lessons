b = input("Введите что-нибудь:")
h = "замена в строке"
a = "Это строка в которую {} новую строку"
print(a.format(b))
a = a.format(h)
print(a)
print(len(a))
if a.find("строка"):
    print("Yes")
else:
    print("No")

