def sumaDig(x):
    if x / 10 == 0:
        return x
    else:
        return x % 10 + sumaDig(x / 10)
