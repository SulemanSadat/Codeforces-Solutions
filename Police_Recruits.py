events = int(input())
hired_crimes = map(int, input().split())
untreated = 0
hired = 0
crime = 0
for amount in hired_crimes:
    if amount > 0:  # Police Hired
        hired += amount
    if amount < 0:  # Crime Happened
        crime += amount
        # if hired < crime:
        untreated += 1

print(untreated)
