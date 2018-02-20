def division(m, n):
    if m < n:
        return 0
    else:
        return 1 + division(m - n, n)
