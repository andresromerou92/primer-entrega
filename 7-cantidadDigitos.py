def canDigitos(m):
    if m / 10 == 0:
    
        return 1
    else:
        return 1 + icanDigitos(m / 10)

