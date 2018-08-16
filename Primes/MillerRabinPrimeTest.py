from random import randrange

def MillerRabin(p):
    d = p-1
    powerOf2 = 0

    while d%2 == 0:
        d //= 2
        powerOf2 += 1
    
    a = randrange(2, p-1)
    x = (a**d) % p
    if x == 1 or x == (p-1):
        return True