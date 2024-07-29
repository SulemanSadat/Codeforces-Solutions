participant, limit = map(int, input().split())

numbers = input().split()
highRanks = []
for num in numbers:
    if int(num) > limit:
        highRanks.append(num)
print(len(highRanks))
