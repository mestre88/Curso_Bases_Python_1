import math

def raizes (a,b,c):
    deltaaux =  b**2 - 4 * a * c
    if deltaaux < 0 :
        print("A função não tem raizes reais")
    else:
        deltaa = math.sqrt(deltaaux)

    if deltaaux == 0:
        raizespos = (-b + deltaa) / (2*a)
        print("A função tem apenas uma raiz com o valor: ", raizespos)
    if deltaaux > 0:
        raizespos = (-b + deltaa) / (2*a)
        raizesneg = (-b - deltaa) / (2*a)
        print("A função tem duas raiz com o valor: ", raizespos, " e o valor: ",raizesneg)
