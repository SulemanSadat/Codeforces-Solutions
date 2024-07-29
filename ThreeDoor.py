for _ in range(int(input())):
    yourKey = int(input())
    behind = input().split()
    zero = behind.index('0')
    if zero == 2: #right
        for a in behind[::-1]:
            print(behind[::-1])
            if a == 1:
                continue
            elif a != 1:
                print("NO")
                break

    elif zero == 0: # left
        for b in behind:
            if b == 0:
                continue
            if b == 1 and yourKey == 2:

                print("YES")




