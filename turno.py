PECAS_BRANCAS = "♔♕♖♗♘♙"
PECAS_PRETAS = "♚♛♜♝♞♟"


def controlar_turno(turno, peca) -> bool:
    if turno == "brancas":
        return peca in PECAS_BRANCAS
    if turno == "pretas":
        return peca in PECAS_PRETAS
    return False


def trocar_turno(turno) -> str:
    if turno == "brancas":
        return "pretas"
    if turno == "pretas":
        return "brancas"
    return turno

