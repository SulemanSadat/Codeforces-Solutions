for _ in range(int(input())):
    polyCoins = int(input())
    c1 = polyCoins // 3
    c2 = c1
    if polyCoins % 3 == 1:
        c1 +=1
    elif polyCoins % 3 == 2:
        c2 +=1
    print(c1, c2)
