def canDigitos(m):
    if m/ 10 == 0:
        return 1
    else:
        return 1 + canDigitos(m / 10)
 
def invertir(m):
    if canDigitos(m) == 1:
        return m
    else:
        return (m % 10) * 10 ** (canDigitos(m) - 1) + invertir(m / 10)
