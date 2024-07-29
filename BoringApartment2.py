target = ''
for _ in range(int(input())):
    apartment = int(input())
    for No in range(1, 10):
        for length in range(1, 5):
            var = f'{No}' * length
            target += var
            if apartment == int(var):
                print(int(len(target)))
                break
    target = ''
