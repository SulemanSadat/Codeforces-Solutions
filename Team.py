count = 0
for _ in range(int(input())):
    petya, vasya, tonya = map(int, input().split())
    if petya and vasya == 1 or petya and tonya == 1 or vasya and petya == 1 or vasya and tonya == 1 or petya and vasya and tonya == 1:
        count += 1
print(count)
