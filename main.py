from tabuleiro import criar_tabuleiro, mostrar_tabuleiro, posicao_valida, mover_peca
from turno import controlar_turno, trocar_turno


PECAS_BRANCAS = "♔♕♖♗♘♙"
PECAS_PRETAS = "♚♛♜♝♞♟"
TIPO_PECAS = {
    "♙": "p", "♟": "p",
    "♖": "t", "♜": "t",
    "♗": "b", "♝": "b",
    "♕": "d", "♛": "d",
    "♔": "r", "♚": "r",
    "♘": "c", "♞": "c",
}


def cor_peca(peca):
    if peca in PECAS_BRANCAS:
        return "brancas"
    if peca in PECAS_PRETAS:
        return "pretas"
    return None


def caminho_livre(tabuleiro, origem, destino):
    """Verifica obstruções em movimentos retos ou diagonais."""
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino

    if origem == destino:
        return False

    diferenca_linha = abs(linha_destino - linha_origem)
    diferenca_coluna = abs(coluna_destino - coluna_origem)

    if not (linha_origem == linha_destino or
            coluna_origem == coluna_destino or
            diferenca_linha == diferenca_coluna):
        return False

    passo_linha = 0 if linha_destino == linha_origem else (
        1 if linha_destino > linha_origem else -1
    )
    passo_coluna = 0 if coluna_destino == coluna_origem else (
        1 if coluna_destino > coluna_origem else -1
    )

    linha = linha_origem + passo_linha
    coluna = coluna_origem + passo_coluna

    while (linha, coluna) != (linha_destino, coluna_destino):
        if tabuleiro[linha][coluna] != ".":
            return False
        linha += passo_linha
        coluna += passo_coluna

    return True


def movimento_valido(tabuleiro, origem, destino, turno):
    """Valida uma jogada conforme a peça, turno e conteúdo do destino."""
    if not posicao_valida(origem) or not posicao_valida(destino):
        print("Movimento inválido: posição fora do tabuleiro.")
        return False

    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino
    peca = tabuleiro[linha_origem][coluna_origem]

    if peca == ".":
        print("Não há peça na casa de origem.")
        return False

    if not controlar_turno(turno, peca):
        print("Essa peça não pertence ao jogador da vez.")
        return False

    peca_destino = tabuleiro[linha_destino][coluna_destino]
    cor_origem = cor_peca(peca)
    cor_destino = cor_peca(peca_destino)

    if cor_destino is not None and cor_origem == cor_destino:
        print("Não é possível capturar uma peça da mesma cor.")
        return False

    tipo = TIPO_PECAS.get(peca)
    diferenca_linha = linha_destino - linha_origem
    diferenca_coluna = coluna_destino - coluna_origem

    if tipo == "p":
        direcao = -1 if cor_origem == "brancas" else 1
        linha_inicial = 6 if cor_origem == "brancas" else 1

        if diferenca_coluna == 0:
            if diferenca_linha == direcao:
                valido = peca_destino == "."
            elif diferenca_linha == 2 * direcao:
                linha_intermediaria = linha_origem + direcao
                valido = (linha_origem == linha_inicial and
                          tabuleiro[linha_intermediaria][coluna_origem] == "." and
                          peca_destino == ".")
            else:
                valido = False
        else:
            valido = (abs(diferenca_coluna) == 1 and
                      diferenca_linha == direcao and
                      cor_destino is not None and
                      cor_destino != cor_origem)

    elif tipo == "t":
        reto = linha_origem == linha_destino or coluna_origem == coluna_destino
        valido = reto and caminho_livre(tabuleiro, origem, destino)

    elif tipo == "b":
        diagonal = abs(diferenca_linha) == abs(diferenca_coluna)
        valido = diagonal and caminho_livre(tabuleiro, origem, destino)

    elif tipo == "d":
        reto = linha_origem == linha_destino or coluna_origem == coluna_destino
        diagonal = abs(diferenca_linha) == abs(diferenca_coluna)
        valido = (reto or diagonal) and caminho_livre(tabuleiro, origem, destino)

    elif tipo == "r":
        valido = max(abs(diferenca_linha), abs(diferenca_coluna)) == 1

    elif tipo == "c":
        valido = ((abs(diferenca_linha) == 2 and abs(diferenca_coluna) == 1) or
                  (abs(diferenca_linha) == 1 and abs(diferenca_coluna) == 2))

    else:
        valido = False

    if not valido:
        print("Movimento inválido para essa peça.")

    return valido


def simular_partida():
    """Executa uma partida simplificada com jogadas válidas e inválidas."""
    tabuleiro = criar_tabuleiro()
    turno_atual = "brancas"

    jogadas = [
        ((6, 4), (4, 4), "1. Peão branco avança de E2 para E4", True),
        ((1, 3), (3, 3), "2. Peão preto avança de D7 para D5", True),
        ((4, 4), (3, 3), "3. Peão branco captura o peão preto", True),
        ((0, 6), (2, 5), "4. Cavalo preto move de G8 para F6", True),
        ((7, 6), (5, 5), "5. Cavalo branco move de G1 para F3", True),
        ((1, 2), (2, 2), "6. Peão preto avança de C7 para C6", True),
        ((7, 5), (4, 2), "7. Bispo branco move de F1 para C4", True),
        ((0, 2), (4, 6), "8. Bispo preto move de C8 para G4", True),
        ((7, 3), (6, 4), "9. Dama branca move de D1 para E2", True),
        ((1, 4), (2, 4), "10. Peão preto avança de E7 para E6", True),
        ((6, 7), (4, 7), "11. Peão branco avança de H2 para H4", True),
        ((0, 4), (1, 4), "12. Rei preto move de E8 para E7", True),
        ((7, 7), (3, 7), "13. Tentativa inválida: torre obstruída pelo peão em H4", False),
        ((7, 7), (5, 7), "14. Torre branca move de H1 para H3", True),
        ((0, 1), (2, 0), "15. Cavalo preto move de B8 para A6", True),
        ((7, 4), (7, 3), "16. Rei branco move de E1 para D1", True)
    ]

    jogadas_validas = 0
    capturas = 0

    print("\n=== Simulação automática da partida ===")

    for origem, destino, descricao, deve_ser_valida in jogadas:
        print("\n" + descricao)

        valido = movimento_valido(tabuleiro, origem, destino, turno_atual)

        if deve_ser_valida:
            if valido:
                peça_origem = tabuleiro[origem[0]][origem[1]]
                peça_destino = tabuleiro[destino[0]][destino[1]]

                if peça_destino != ".":
                    capturas += 1
                    print("Captura realizada:", peça_origem, "captura", peça_destino)

                mover_peca(tabuleiro, origem, destino)
                jogadas_validas += 1
                print("Movimento válido:", origem, "->", destino)

                turno_atual = trocar_turno(turno_atual)
                print("Novo turno:", turno_atual)
            else:
                print("Erro: esta jogada deveria ser válida.")
        else:
            if valido:
                print("Erro: esta jogada deveria ser inválida.")
            else:
                print("Tentativa inválida corretamente rejeitada:")
                print("A torre encontrou obstrução ou uma casa ocupada.")

        mostrar_tabuleiro(tabuleiro)
        print("Turno atual:", turno_atual)

    print("\nResumo da simulação:")
    print("Jogadas válidas realizadas:", jogadas_validas)
    print("Capturas realizadas:", capturas)


def main():
    """Executa apenas a simulação automática da partida."""
    simular_partida()


if __name__ == "__main__":
    main()

