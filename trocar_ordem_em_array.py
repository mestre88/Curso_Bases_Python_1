

def inverter_ordem (lista,i):
    lista_inversa = []
    while i > 0:
        lista_inversa.append(lista[i-1])
        i = i - 1
    return lista_inversa






lista = []
numero = int(input("Insere numeros inteiros para a lista ou array: "))
i = 0
while (numero != 0):
    lista.append(numero)
    numero = int(input("Para terminar insere o numero 0: "))
i = len(lista)
lista = inverter_ordem(lista,i)
print(lista)




    
