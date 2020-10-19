"""
    Tady budou funkce pro načítání a tištění šachovnice.

    Mimochodem tohle se bude hodit:
    print("\33[41m" + "--" + "\33[0m")
"""


def load_board(raw):
    """
        Dostane textovou reprezentaci šachovnice
        a vrátí její list-ovou reprezentaci
    """
    return [line.split() for line in raw.splitlines()]


def print_board(board, highlighted=[]):
    """Dostane šachovnici a vytiskne ji na obrazovku"""
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if (row_index, cell_index) in highlighted:
                print("\33[41m" + cell + "\33[0m", end="")
            else:
                print(cell, end="")

            print(" ", end="")
        print()
