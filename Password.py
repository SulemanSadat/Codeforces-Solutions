import math as S

for _ in range(int(input())):
    length = int(input())
    non_Used = map(int, input().rstrip().split())
    main = 10 - len(list(non_Used))
    sub = S.factorial(main - 2) * 2
    print((S.factorial(main) // sub) * 6)  # 0 1 2 4 5 6 8 9

