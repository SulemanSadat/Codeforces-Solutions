numbers = input()
for a in numbers:
    if a == '+':
        numbers = numbers.replace('+', '')
result = sorted(numbers)
result = '+'.join(result)
print(result)