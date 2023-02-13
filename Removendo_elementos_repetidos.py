def remove_repetidos (lista):
    x = 0
    y = 1
    cumprimento = len(lista) - 1
    while x < cumprimento:
        while y <= cumprimento:
            if lista[x] == lista[y]:
                del lista[y]
                cumprimento = cumprimento - 1
            else:
                y = y+1
        x = x+1
        y = x+1
        
    lista.sort()
    print (lista)
    return lista

