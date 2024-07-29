find = int(input())
factor = 1
counter = 0
for f in range(1, 1000 + 1):
    factor *= f
    for g in str(factor)[::-1]:
        if g == '0':
            counter += 1
        elif g != '0':
            break
    if int(counter) == find:
        print(f)
        break
    counter = 0
