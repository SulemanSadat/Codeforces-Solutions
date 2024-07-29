word = input()
length_upper = 0
length_lower = 0
for w in word:
    if w == w.upper():
        length_upper += 1
    if w == w.lower():
        length_lower += 1
if length_upper > length_lower:
    print(word.upper())
else:
    print(word.lower())
