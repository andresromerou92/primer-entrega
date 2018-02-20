def producto(m,n):
    if m==1:
        return n
    else:
        return n + producto(m-1,n)
