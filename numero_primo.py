
def primo (n):
    m = 2
    resto = 1
    if n > 2:
        while resto != 0 and m < n :
            resto = n % m
            m = m + 1
        if resto == 0:
            print ("O numero não é Primo")
            return False
        else:
            print ("O numero é primo!")
            return True
    else:
        if n < 2:
            print ("O numero não é primo!")
            return False
        if n == 2:
            print ("O numero é primo!")
            return True
        
