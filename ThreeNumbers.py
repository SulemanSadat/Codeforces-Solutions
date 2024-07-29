import random

numbers = map(int, input().split())
for num in numbers:
    r = random.randint(1)
    if num == sum(r):
        print(r)
