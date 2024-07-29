orange = int(input())
percentage = map(int, input().split())
result = 0
for p in percentage:
    result += p
print(result / orange)
