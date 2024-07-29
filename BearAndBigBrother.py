count = 0
Limak, Bob = map(int, input().split())
if Limak <= Bob:
    for year in range(1, 10):
        Limak *= 3
        Bob *= 2
        if Limak > Bob:
            count += year
            break
print(count)
