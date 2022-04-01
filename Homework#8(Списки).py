high_list = [110, 150, 101, 181, 154, 198, 105, 173, 102, 101, 101]

Petr_high = int(input("Рост Пети:"))

high_list.append(Petr_high)

high_list.sort(reverse=True)

print(high_list)

for i in range(0, len(high_list)):
    if high_list[i] == Petr_high:
        print(high_list.index(Petr_high) + high_list.count(Petr_high))
        break


