
numero = int(input("Digite um numero inteiro: "))
restonumero = 1
restonumeroseguinte = 1
VerificaAdjacente = False

while VerificaAdjacente == False and numero != 0:
    restonumero = numero % 10
    numero = numero // 10
    restonumeroseguinte = numero % 10
    
    
    print(restonumero,restonumeroseguinte)
    
    if restonumero == restonumeroseguinte:
        VerificaAdjacente = True

if VerificaAdjacente :
    print ("Existem numeros adjacentes iguais! ")
else:
    print ("Não Existem numeros adjacentes iguais! ")