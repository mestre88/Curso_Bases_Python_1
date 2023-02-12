largura = 0
altura = 0
while largura <= 1:
    largura = int(input("digite a largura: "))
while altura <= 1:
    altura = int(input("digite a altura: "))
aux_largura = largura
while altura > 0:
    while aux_largura > 0:
        print("#", end = '')
        aux_largura = aux_largura - 1
    altura = altura - 1
    aux_largura = largura
    print("")
