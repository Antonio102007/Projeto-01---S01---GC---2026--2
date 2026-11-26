#movimento do rei desde no início da partida 
def movimento_rei(tabuleiro, origem, destino) -> bool: 
    linha_origem = origem[0]
    coluna_origem = origem[1]

    linha_destino = destino[0]
    coluna_destino = destino[1]

#recebe origem (0,1) destino (0,1)
 
    dif_linha = abs(linha_destino - linha_origem)
    dif_coluna = abs(coluna_destino - coluna_origem)


    if dif_linha <= 1 and dif_coluna <=1:
        if dif_linha != 0 or dif_coluna != 0:
            return True 

    return False


def movimento_cavalo(tabuleiro, origem, destino) -> bool:
    linha_origem = origem[0]
    coluna_origem = origem[1]

    linha_destino = destino[0]
    coluna_destino = destino[1]

    dif_linha = abs(linha_destino - linha_origem)
    dif_coluna = abs(coluna_destino - coluna_origem)

    if (dif_linha == 2 and dif_coluna == 1) or (dif_linha == 1 and dif_coluna == 2):
        return True

    return False

