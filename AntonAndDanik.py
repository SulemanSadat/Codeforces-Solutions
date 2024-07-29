games = int(input())
name = input()
Anton = 0
Danik = 0
for char in name:
    if char == 'A':
        Anton += 1
    elif char == 'D':
        Danik += 1
if Anton > Danik:
    print('Anton')
elif Danik > Anton:
    print('Danik')
elif Anton == Danik:
    print('Friendship')

