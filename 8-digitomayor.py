def mayor(n):

    digmay = n%10

    while n > 0:

        if n%10 > digmay:

            digmay = n%10

        n //= 10

    return digmay

print (mayor(75))
