def sumUpDigits(inputString):

    answer = 0

    for i in range(len(inputString)):
        if '1' <= inputString[i] and inputString[i] <= '9':
            answer += ord(inputString[i]) - ord('1')

    return answer
