def caminho_livre( 
    tabuleiro: list[list[str]],
    origem: tuple[int, int],
    destino: tuple[int, int], 
) -> bool:
    '''
    Verifica se todas ass casas intermediárias entre origem e destinoestão vazias.
    nota: Não verifica a casa de origem nem a cadas de destino (pois o destino pode conter uma peça adversária para capturar, validada em capturas.py)
    '''
    #Desempacota as tuplas de coordenadas em variáveis separadas para facilitar a leitura

    l1, c1 = origem  # l1 = linha inicial, c1 = coluna inicial
    l2, c2 = destino # l2 = linha destino, c2 = coluna destino

    #Calcular a distancia absoluta (sem sinal negativo) percorre em linhas e colunas
    dist_l = abs(l2 - l1)
    dist_c = abs(c2 - c1)

    #Trava de segurança: garante que o trajeto forme uma linha reta (horizontal/vertical)
    #ou uma diagonal perfeita. Isso evita um loop infinito caso a fução seja chamada
    #com coordenadas aleatorias (ex: movimento em "L" de cavalo).
    if not (l1 == l2 or c1 == c2 or dist_l == dist_c):
        return False

    #--- Calculo da direção do deslocamento (passo de -1, 0 ou 1)---
    #LINHA
    if l2 > l1: 
        passo_l = 1 #Está descendo no tabuleiro (aumenta o ídice da linha) 
    elif l2 < l1: 
        passo_l = -1 # Está subindo no tabuleiro (diminue o índice da linha)
    else: 
        passo_l = 0 # Continua na mesma linha (movimento horizontal)

    #COLUNA
    if c2 > c1:
        passo_c = 1 #Está indo para a direta (aumenta o indice da coluna)
    elif c2 < c1:
        passo_c = -1 #Está indo para a esquerda (dimunue o indice da coluna)
    else:
        passo_c = 0 #Está na mesma coluna (movimento vertical)

    #---Caminhada por casa no tabuleiro---
    # Define a primeira casa intermediária, pulando a casa de origem onde a peça está
    l_atual = l1 + passo_l
    c_atual = c1 + passo_c

    #Continua avançando enquanto não alcança a coordenada exara de destino
    while (l_atual, c_atual) != (l2, c2):
        #Se na casa atual não contiver ".", significa que há uma peça no meio do caminho
        if tabuleiro[l_atual][c_atual] != ".":
            return False # Caminho obstrído!

        #Avança mais uma casa na direção calculada
        l_atual += passo_l
        c_atual += passo_c
    #Se saiu do laço sem encontrar nenhuma peça no trajeto, o caminho está liver
    return True


def movimento_torre(
    tabuleiro: list[list[str]],
    origem: tuple[int, int],
    destino: tuple[int, int],
) -> bool:
    """
    Valida o movimento da Torre: anda apenas em linha reta (horizontal ou vertical)
    por quantas casas quiser, desde que não haja obstruções.
    """
    # Impede que a peça seja "movida" para a mesma casa onde já está
    if origem == destino:
        return False

    # Extrai linha e coluna de origem e destino
    l1, c1 = origem
    l2, c2 = destino

    # Para andar em linha reta, OU a linha permanece igual (horizontal)
    # OU a coluna permanece igual (vertical). Se ambas mudarem, não é movimento de Torre.
    if l1 != l2 and c1 != c2:
        return False

    # Se a geometria está certa, delega a verificação de bloqueios para caminho_livre()
    return caminho_livre(tabuleiro, origem, destino)


def movimento_bispo(
    tabuleiro: list[list[str]],
    origem: tuple[int, int],
    destino: tuple[int, int],
) -> bool:
    """
    Valida o movimento do Bispo: anda apenas nas diagonais por quantas casas
    quiser, desde que não haja obstruções.
    """
    # Impede movimento nulo (ficar parado na mesma casa)
    if origem == destino:
        return False

    # Extrai linha e coluna de origem e destino
    l1, c1 = origem
    l2, c2 = destino

    # Em qualquer diagonal da matriz, a quantidade de linhas andadas deve ser
    # exatamente igual à quantidade de colunas andadas (ex: 3 linhas e 3 colunas).
    if abs(l2 - l1) != abs(c2 - c1):
        return False

    # Se a geometria diagonal está certa, verifica se o trajeto está desimpedido
    return caminho_livre(tabuleiro, origem, destino)


def movimento_dama(
    tabuleiro: list[list[str]],
    origem: tuple[int, int],
    destino: tuple[int, int],
) -> bool:
    """
    Valida o movimento da Dama (Rainha): combina os movimentos da Torre e do Bispo,
    podendo andar em linha reta ou na diagonal sem pular peças.
    """
    # Reaproveita as funções já criadas: se o movimento for válido como Torre
    # OU válido como Bispo (incluindo checagem de obstrução), é válido para a Dama.
    return movimento_torre(tabuleiro, origem, destino) or movimento_bispo(
        tabuleiro, origem, destino
    )



        