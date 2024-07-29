center = 0
for _ in range(5):
    matrix = input().split()
    for col in matrix:
        if col == '1':
            find_number_1 = matrix.index(col) - 1
            if matrix.index(col) > 2:
                while center < find_number_1:
                    center += 1
                col.replace('1', '0')
            if matrix.index(col) < 2:
                while center < find_number_1:
                    center += 1
                col.replace('1', '0')
print(center)
