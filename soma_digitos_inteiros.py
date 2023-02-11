
n = int(input("Digite um número inteiro: "))
soma = 0
resto = 1

while n != 0:
    resto = n % 10
    n = n // 10
    soma = soma + resto
print(soma)
