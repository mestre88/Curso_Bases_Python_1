def fatorial (n):
    fat = n
    if n > 1:
        while n > 1 :
            n = n - 1
            fat = fat * n
    else:
        if n == 0 or n == 1:
            fat = 1

    return fat

def Numbinomial (n,k):
    return fatorial(n)/((fatorial(k))*(fatorial(n-k)))
    
