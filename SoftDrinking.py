try:
    n, k, l, c, d, p, nl, np = map(int, input().split())
    drink = k * l
    toast = drink // n
    limes = c * d
    salt = p // np
    print(min(toast, limes, salt) // n)

except ZeroDivisionError:
    print(0)
