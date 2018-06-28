def newNumeralSystem(number):
    number = ord(number)
    output = []
    for i in range(ord('A'),(number-ord('A'))//2+ord('A')+1):
        output.append(chr(i)+" + "+chr(number-i+ord('A')))
    
    return output