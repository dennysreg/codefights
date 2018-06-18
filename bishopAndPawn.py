def bishopAndPawn(bishop, pawn):

    def getX(pos):
        return ord(pos) - ord('a')
    def getY(pos):
        return ord(pos) - ord('1')

    x1 = getY(bishop[0])
    y1 = getY(bishop[1])
    x2 = getX(pawn[0])
    y2 = getY(pawn[1])

    if x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
        return True

    return False
