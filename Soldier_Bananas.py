result = 0
pay, dollars, bananas = map(int, input().split())
for i in range(1, bananas + 1):
    r = pay * i
    result += r
print(result - dollars)
