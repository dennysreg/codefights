def countInversionsNaive(inputArray):

    result = 0

    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            if inputArray[i] >= inputArray[j]:
                result += 1
    return result