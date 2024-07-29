result = 0
amount, fence = map(int, input().split())
PersonsHeight = map(int, input().split())
for heights in PersonsHeight:
    if heights <= fence:
        result += 1
    elif heights > fence:
        result += 2
print(result)
