spend = 0
n = input()
citizens = list(map(int, input().split()))
max_value = max(citizens)
for citizen in citizens:
    if citizen < max_value:
        spend += max_value - citizen
print(spend)
