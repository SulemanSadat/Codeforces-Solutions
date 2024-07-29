PeopleLenght = int(input())
easy = 0
hard = 0
review = map(int, input().split())
for result in review:
    if result == 0:
        easy = 0
    elif result == 1:
        hard = 1
if hard > easy:
    print('HARD')
elif easy < hard:
    print('EASY')
else:
    print('EASY')
