        
def fatorial (valor):
    n = 1
    while valor > 1:
        n = n * valor
        valor = valor - 1
    return n



n = 1
valor = int(input("Digite o valor para calcular o fatorial: "))
while valor >= 0:
    n = fatorial(valor)
    print("O valor do fatorial é: ",n)
    n = 1
    valor = int(input("Digite o valor para calcular o fatorial: "))
print("Numero negativo! Adeus! bye! see you!")
