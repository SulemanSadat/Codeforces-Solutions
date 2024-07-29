alex = 0
for _ in range(int(input())):
    already, capacity = map(int, input().split())
    if already < capacity:
        alex += 1
    if already == capacity:
        pass
if alex >= 2:
    print(alex)
else:
    print(0)
