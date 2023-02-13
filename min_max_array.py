
def minmax (temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "C.")

def maxima(temps):
    max = temps[0]
    i = 1
    while i > len(temps):
        if temps[i] < max:
            max = temps[i]
        i = i+1
    return max

def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i+1
    return min

def teste_pontual(temp,valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("valor errado para array ", temp)
        print("valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)

def teste_minima():
    print("Iniciando os testes")
    for x in range(0,len(lista_testes_temp)-1,2):
        teste_pontual(lista_testes_temp[x],lista_testes_temp[x+1])
    
    print("Finalizando os testes")

lista_testes_temp = [[0],0,[0,0,0,0,0],0,[0,1,2,3,4],0,[-15, -10, -5, 0, 1, 2, 3, 4], -15]


