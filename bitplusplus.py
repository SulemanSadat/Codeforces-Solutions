x = 0
for _ in range(int(input())):
    statement = input()
    if '++' in statement:
        x += 1
    elif '--' in statement:
        x -= 1
print(x)
