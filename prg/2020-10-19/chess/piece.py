"""
    Tady budou funkce pro získávání možných tahů pro každou figurku.
"""

def get_possible_targets(board, tile):
    piece_type = get_piece_type(board[tile[0]][tile[1]])

    if piece_type == "P":
        return get_possible_targets_for_pawn(board, tile)
    elif piece_type == "R":
        exit("Not implemented.")
    elif piece_type == "N":
        exit("Not implemented.")
    elif piece_type == "B":
        exit("Not implemented.")
    elif piece_type == "Q":
        exit("Not implemented.")
    elif piece_type == "K":
        exit("Not implemented.")
    else:
        exit("There's no piece on the given tile.")

def get_piece_type(piece):
    return piece[1]

def get_possible_targets_for_pawn(board, tile):
    return [(4, 5), (3, 5)] # dummy, nestihli jsme implementovat
