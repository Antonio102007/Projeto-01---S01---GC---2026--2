def movimento_peao(tabuleiro, origem, destino) -> bool:
    # onde esta o peao 
    linhainicial = origem[0]
    colunainicial = origem[1]

    # aonde o usuario pretende ir
    linhadestino = destino[0]
    colunadestino = destino[1]

    # qual peao que é no tabuleiro
    peca = tabuleiro[linhainicial][colunainicial]

    if peca.isupper():
        # branco
        direcao = -1
    else:
        # preto
        direcao = 1

    # movimento normal
    if colunainicial == colunadestino:
        if linhainicial - linhadestino == direcao:
            if tabuleiro[linhadestino][colunadestino] == ".":
                return True

    # movimento de começo, 2 casas
    if peca.isupper():
        # branco
        if linhainicial == 6:
            if colunainicial == colunadestino:
                if linhainicial - linhadestino == direcao*2:
                    if tabuleiro[linhainicial + direcao][colunainicial] == ".":
                        if tabuleiro[linhadestino][colunadestino] == ".":
                            return True
    else:
        # preto
        if linhainicial == 1:
            if colunainicial == colunadestino:
                if linhainicial - linhadestino == direcao*2:
                    if tabuleiro[linhainicial + direcao][colunainicial] == ".":
                        if tabuleiro[linhadestino][colunadestino] == ".":
                            return True

    # captura
    if peca.isupper():
        # branco
        if linhainicial - linhadestino == direcao:
            if colunainicial - colunadestino == 1 or colunainicial - colunadestino == -1:
                if tabuleiro[linhadestino][colunadestino] != ".":
                    if tabuleiro[linhadestino][colunadestino].islower():
                        return True
    else:
        # preto
        if linhainicial - linhadestino == direcao:
            if colunainicial - colunadestino == 1 or colunainicial - colunadestino == -1:
                if tabuleiro[linhadestino][colunadestino] != ".":
                    if tabuleiro[linhadestino][colunadestino].isupper():
                        return True
    return False

    
