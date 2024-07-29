def fast(num1, num2):
    answer = ""
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            answer += "1"
        else:
            answer += '0'
    return answer


num1 = input()
num2 = input()

ans = fast(num1, num2)
print(ans)
