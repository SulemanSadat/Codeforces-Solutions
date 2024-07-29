k1, k2, k3, k4 = map(int, input().split())
favorite = ['2', '3', '5', '6']
arr = list(f"{k1 * '2'}{k2 * '3'}{k3 * '5'}{k4 * '6'}")
value = 0
for i in arr:
    if str(2) in arr and str(5) in arr and str(6) in arr:
        arr.remove('2')
        arr.remove('5')
        arr.remove('6')
        value += 256
    elif str(3) in arr and str(2) in arr:
        arr.remove('3')
        arr.remove('2')
        value += 32
    else:
        break
print(value)
