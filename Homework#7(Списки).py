import random
a = [random.randint(0, 1000) for x in range(15)]
positive_compare_counter = 0

print(a)

for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        positive_compare_counter += 1

print(positive_compare_counter)
