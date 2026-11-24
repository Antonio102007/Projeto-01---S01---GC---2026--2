
def criar_tabuleiro():
    """
    Cria o tabuleiro com as peças nas posições iniciais.

    Retorna:
        list: matriz 8x8.
    """

    # Letras maiúsculas são as brancas e minúsculas são as pretas
    tabuleiro = [
        ["t", "c", "b", "d", "r", "b", "c", "t"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["T", "C", "B", "D", "R", "B", "C", "T"]
    ]

    return tabuleiro


def mostrar_tabuleiro(tabuleiro):
    """
    Mostra o tabuleiro no terminal.

    Parâmetros:
        tabuleiro (list)

    Retorna:
        None
    """

    print("    0 1 2 3 4 5 6 7")
    print("   -----------------")

    # Percorre as linhas e colunas
    for linha in range(8):
        print(linha, "|", end=" ")

        for coluna in range(8):
            print(tabuleiro[linha][coluna], end=" ")

        print("|")

    print("   -----------------")


def posicao_valida(pos):
    """
    Verifica se a posição está dentro do tabuleiro.

    Parâmetros:
        pos (tuple)

    Retorna:
        bool
    """

    linha = pos[0]
    coluna = pos[1]

    # Verifica os limites do tabuleiro
    if linha >= 0 and linha <= 7 and coluna >= 0 and coluna <= 7:
        return True
    else:
        return False


def mover_peca(tabuleiro, origem, destino):
    """
    Move uma peça da origem para o destino.
    O movimento deve ser validado antes.

    Parâmetros:
        tabuleiro (list)
        origem (tuple)
        destino (tuple)

    Retorna:
        None
    """

    linha_origem = origem[0]
    coluna_origem = origem[1]

    linha_destino = destino[0]
    coluna_destino = destino[1]

    # Coloca a peça na nova posição
    tabuleiro[linha_destino][coluna_destino] = tabuleiro[linha_origem][coluna_origem]

    # Deixa a posição anterior vazia
    tabuleiro[linha_origem][coluna_origem] = "."


# Teste individual do tabuleiro
if __name__ == "__main__":
    tabuleiro = criar_tabuleiro()

    print("Tabuleiro inicial:")
    mostrar_tabuleiro(tabuleiro)

    print("\nTeste de posições:")
    print(posicao_valida((6, 4)))
    print(posicao_valida((8, 4)))

    mover_peca(tabuleiro, (6, 4), (4, 4))

    print("\nTabuleiro depois do movimento:")
    mostrar_tabuleiro(tabuleiro)
