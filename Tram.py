start = 0
items = []
for stops in range(int(input())):
    exits, enter = map(int, input().split())
    start += enter
    start -= exits
    items.append(start)
print(max(items))
