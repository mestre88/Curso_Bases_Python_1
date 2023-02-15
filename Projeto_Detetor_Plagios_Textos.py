import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    sab = 0.0
    for x in range(0,len(as_a)-1):
        sab = sab + abs(as_a[x] - as_b[x])
    sab = sab / len(as_a)
    
    return sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = []
    frases = []
    lista_palavras = []
    lista_palavras_total = []
    lista_frases_total = []

    n_carateres_frases_total = 0

    n_palavras_frases_total = 0
    n_palavras_diferentes_total = 0
    n_palavras_unicas_total = 0

    n_frases_total = 0

    n_sentencas_total = 0
    n_carateres_sentencas_total = 0

    wal = 0.0
    ttr = 0.0
    hlr = 0.0
    sal = 0.0
    sac = 0.0
    pal = 0.0



    sentencas = separa_sentencas(texto)
    for j in range (0,len(sentencas)):
        frases = separa_frases(sentencas[j])
        lista_frases_total = lista_frases_total + frases
        n_carateres_sentencas_total = n_carateres_sentencas_total + len (sentencas[j])
        for k in range (0,len(frases)):
            lista_palavras = separa_palavras(frases[k])
            ''' contar nº caracteres '''
            for s in range (0,len(lista_palavras)):
                n_carateres_frases_total = n_carateres_frases_total + len (lista_palavras[s])
            lista_palavras_total = lista_palavras_total + lista_palavras

        ''' contar nº palavras '''
        n_palavras_frases_total = len(lista_palavras_total)
        n_palavras_diferentes_total = n_palavras_diferentes(lista_palavras_total)
        n_palavras_unicas_total = n_palavras_unicas(lista_palavras_total)

    ''' contar frases '''
    n_frases_total = len(lista_frases_total)

    ''' contar nº sentenças '''
    n_sentencas_total = len(sentencas)




    '''Tamanho médio de palavra'''
    wal = n_carateres_frases_total / n_palavras_frases_total

    '''Relação Type-Token'''
    ttr = n_palavras_diferentes_total / n_palavras_frases_total

    '''Razão Hapax Legomana'''
    hlr = n_palavras_unicas_total / n_palavras_frases_total

    '''tamanho médio de sentença'''
    sal = n_carateres_sentencas_total / n_sentencas_total

    '''complexidade média da sentença'''
    sac = n_frases_total / n_sentencas_total

    '''tamanho medio de frase'''
    pal = n_carateres_sentencas_total / n_frases_total

    print("nº caracteres= ",n_carateres_frases_total)
    print("n_palavras_frases_total = ", n_palavras_frases_total)
    print("n_palavras_diferentes_total = ", n_palavras_diferentes_total)
    print("n_palavras_unicas_total = ", n_palavras_unicas_total)
    print("n_frases_total = ", n_frases_total)
    print("n_sentencas_total = ", n_sentencas_total)
    print("Tamanho médio de palavra = ", wal)
    print("Relação Type-Token' = ", ttr)
    print("Razão Hapax Legomana = ", hlr)
    print("tamanho médio de sentença = ", sal)
    print("complexidade média da sentença = ", sac)
    print("tamanho medio de frase = ", pal)
    
    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinatura = []
    avaliação = []
    texto_n = 0
    i = 0
    j = 1
    for x in range (0, len(textos)):
        assinatura = calcula_assinatura (textos[x])
        avaliação.append(compara_assinatura(assinatura, ass_cp))
    if len(avaliação) <= 1:
        return 1
    else:
        while j < len(avaliação)-1:
            if avaliação[i] < avaliação[j]:
                texto_n = i
                j = j + 1
            else:
                texto_n = j
                i = j
                j = j + 1
        texto_n = texto_n + 1
        return texto_n 








ass_cp = le_assinatura()
textos = le_textos()




