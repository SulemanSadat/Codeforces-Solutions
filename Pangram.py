length = int(input())
sentence = input()
print(sentence)
if len(sentence) == len(set(sentence)):
    print("YES")
else:
    print("NO")