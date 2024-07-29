number, amount = map(int, input().split())
for _ in range(amount):
    if number % 10 != 0:
        number -= 1
    else:
        number //= 10
print(number)
