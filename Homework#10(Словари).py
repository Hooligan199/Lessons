a = "В единственной строке записан текст . " \
    "Для каждого слова из данного текст , " \
    "подсчитайте сколько раз оно встречалось в этом тексте."

b = [g.strip().lower() for g in a.split(' ')]

c = {}.fromkeys(b, 0)

print(b)

for i in b:
    if c.get(i, None) is not None:
        c[i] += 1


print(c)
