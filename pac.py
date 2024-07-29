def taskOfPairing(freq):
    pairs = 0
    remaining = 0

    for i in range(len(freq)):
        pairs += (freq[i] + remaining) // 2
        remaining = (freq[i] + remaining) % 2

    return pairs


# Read input
n = int(input())
freq = []
for _ in range(n):
    freq.append(int(input()))

# Call the function and print the result
result = taskOfPairing(freq)
print(result)