meuCartao = int(input("Digite o numero do cartão de crédito: "))

cartaolido = 1
encontreimeucartaonalista = False
while cartaolido != 0 and not encontreimeucartaonalista:
	cartaolido = int(input("Digite o numero do proximo cartão de crédito: "))
	if cartaolido == meuCartao:
			encontreimeucartaonalista = True

if encontreimeucartaonalista:
	print("EBA!o catao esta na lista!")
else:
		print("ups!o catao nao esta na lista!")