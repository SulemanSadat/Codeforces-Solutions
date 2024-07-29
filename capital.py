word = input()
First_letter = word[0]
if First_letter == First_letter.upper():
    print(word)
elif First_letter == First_letter.lower():
    print(word.title())
    print(f"{First_letter.upper()}{word[1::]}")
