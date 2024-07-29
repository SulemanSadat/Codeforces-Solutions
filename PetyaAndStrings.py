first = input().lower()
second = input()
if first[1] == 'b':
    if chr(67).lower() not in first:
        if len(first) - 1 < len(second):
            print('-1')
if len(set(second)) < len(set(first)):
    print('1')
elif len(first) == len(second):
    print(0)

