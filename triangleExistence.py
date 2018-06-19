def triangleExistence(sides):

    sides = sorted(sides)

    if sides[0] + sides[2] > sides[1]:
        return True
    return False
