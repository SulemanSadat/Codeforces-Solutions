count = 0
col, row = map(int, input().split())
square = col * row
for point in range(square):
    if square > 1:
        square -= 2
        count += 1
        # count.append(square)
print(count)
