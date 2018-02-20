def potencia (n,m):
    if m==1: 
        return n
    elif m==0:
        return 1
    else:
        return n*potencia(n,m-1)
