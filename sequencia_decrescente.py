
decrescente = True
anterior = int (input("digite o primeiro numero da sequencia: "))

valor = 1

while valor != 0 and decrescente:
	valor = int (input("digite um numero da sequencia: "))
	if valor > anterior:
		decrescente = False
	anterior = valor
    
if decrescente == True:
    print("A sequencia está em ordem decrescente! :-) ")
else:
    print("A sequencia não está em ordem decrescente")
    