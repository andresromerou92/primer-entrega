def palindromo(n):
   
    centena=n/100
    decena=(n%100)/10
    unidad=(n%100)%10

    if (centena==unidad):
        return "el numero  es palindromo"
           
    else:
        return "el numero NO es palindromo"
     

