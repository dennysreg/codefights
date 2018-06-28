import fractions
def fractionReducing(fraction):
    g = fractions.gcd(fraction[0],fraction[1])
    return [fraction[0]/g,fraction[1]/g]

