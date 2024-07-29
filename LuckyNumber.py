def is_nearly_lucky(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 4 or digit == 7:
            count += 1
        n = n // 10
    return count in [4, 7]

n = int(input())

if is_nearly_lucky(n):
    print("YES")
else:
    print("NO")