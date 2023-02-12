largura = 0
altura = 0
while largura <= 1:
    largura = int(input("digite a largura: "))
while altura <= 1:
    altura = int(input("digite a altura: "))
aux_largura = largura
aux_altura = altura
while aux_altura > 0:
    while aux_largura > 0:
        if aux_largura == 1 or aux_largura == largura or aux_altura == 1 or aux_altura == altura:
            print("#", end = '')
        else:
            print(" ", end = '')
        aux_largura = aux_largura - 1
    aux_altura = aux_altura - 1
    aux_largura = largura
    print("")
