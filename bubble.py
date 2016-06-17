import random

numbers = []
a = 0

while (a < 100):
    b = random.randint(0,10000)
    numbers.append(b)
    a += 1

for c in range(len(numbers)):
    for d in range(c+1, len(numbers)):
        if numbers[c] > numbers[d]:
            temp = numbers[c]
            numbers[c] = numbers[d]
            numbers[d] = temp

print numbers
