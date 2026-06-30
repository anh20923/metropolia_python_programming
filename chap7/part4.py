import random

numbers = []

# Chọn 7 số ngẫu nhiên từ 1 đến 39
while True:
    if len(numbers) == 7:
        break

    pick = random.randint(1, 39)

    if pick not in numbers:
        numbers.append(pick)

numbers.sort()

print("The program picked the following numbers:")

for i in numbers:
    print(i, end=' ')