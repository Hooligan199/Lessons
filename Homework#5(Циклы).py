num = int(input(">>>"))

for i in range(0, num):

  for k in range(0, num-i-1):
    print(end=" ")

  for k in range(0, i+1):
    print(" *", end="")

  print()

