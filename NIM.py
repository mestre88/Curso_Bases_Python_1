


def partida ():
    vez_jogador = False
    vez_computador = False
    n = 1

    while n < 2 or m > n:
        n = int (input ("Quantas peças? "))
        m = int (input("Limite de peças por jogada? "))


    if n % (m+1) == 0 :
        print ("Você começa!\n")
        b = usuario_escolhe_jogada(n,m)
        n = n -  b
        print("Você tirou ",b," peça.\n")
        print("Agora resta apenas ",n," peça no tabuleiro.\n")
        vez_jogador = False
        vez_computador = True
        
    else:
        print ("Computador começa!\n")
        a = computador_escolhe_jogada(n,m)
        n = n - a
        print("O computador tirou ", a," uma peça.\n")
        print("Agora restam ",n," peças no tabuleiro.\n")
        vez_jogador = True
        vez_computador = False

        
    while n > 0:
        if vez_computador:
            a = computador_escolhe_jogada(n,m)
            n = n - a
            print("O computador tirou ", a," uma peça.\n")
            if n > 0 :
                print("Agora restam ",n," peças no tabuleiro.\n")
                vez_jogador = True
                vez_computador = False
            else:
                print ("Fim do jogo! O computador ganhou!\n")
                return 1
                
        if vez_jogador:
            b = usuario_escolhe_jogada(n,m)
            n = n -  b
            print("Você tirou ",b," peça.\n")
            if n > 0 :
                print("Agora resta apenas ",n," peça no tabuleiro.\n")
                vez_jogador = False
                vez_computador = True
            else:
                print ("Fim do jogo! Algo de errado não está certo! Voce utilizador ganhou!\n")
                return 0




    
def computador_escolhe_jogada (n,m):
    PecasaRetirar = m

    if m >= n:
        return n
    else:
        while PecasaRetirar > 0:
            if ((n - PecasaRetirar) % (m+1)) == 0:
                return PecasaRetirar
            else:
                PecasaRetirar = PecasaRetirar - 1
                
    return m





def usuario_escolhe_jogada (n,m):
    PecasaRetirar = int(input("Quantas peças você vai tirar? "))
    while PecasaRetirar > m or PecasaRetirar > n:
        print("Oops! Jogada inválida! Tente de novo.\n")
        PecasaRetirar = int(input("Quantas peças você vai tirar? "))          
    return PecasaRetirar
    








def campeonato ():
    rodada = 1
    vitorias_pc = 0
    vitorias_utilizador = 0
    print("Voce escolheu um campeonato!\n")
    while rodada <= 3:
        print("**** Rodada ",rodada," ****\n")
        a = partida()
        rodada = rodada + 1
        if a == 1:
            vitorias_pc = vitorias_pc + 1
        else:
            vitorias_utilizador = vitorias_utilizador + 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você ",vitorias_utilizador," X ",vitorias_pc," Computador")


print("Bem-vindo ao jogo do NIM! Escolha:\n")
jogo = 0
while  jogo != 1 and jogo != 2:
    jogo = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

if jogo == 1:
    partida()
if jogo == 2:
    campeonato()






