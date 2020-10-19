"""
    Řekněme, že programujeme šachy. Součástí takové hry bude jistě
    i komponenta, která pro daný stav šachovnice a vybranou figurku
    vrátí seznam pozic na šachovnici, kam lze s figurkou táhnout.

    Seznam pozic musí vzít v potaz barvy figurek, jejich sbírání apod.
"""

from board import *
from piece import get_possible_targets

# INPUT

board_raw = """\
BR BN BB BQ BK BB BN BR
BP BP BP BP BP BP BP BP
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
-- -- -- -- -- -- -- --
WP WP WP WP WP WP WP WP
WR WN WB WQ WK WB WN WR\
"""

tile = (6, 5)

# MAIN

board = load_board(board_raw)
targets = get_possible_targets(board, tile)

# OUTPUT

print_board(board, targets)
