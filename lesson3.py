с = "замена в строке"
b = input("Введите что нибудь:")
a = "Это строка в которую {} новую строку"
print(a.format(b))
h = "Это строка в которую {} новую строку"
print(h.format(с))
print(len(a))
if a.find("строка"):
    print("Yes")
else:
    print("No")

