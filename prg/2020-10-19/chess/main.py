"""
    Řekněme, že programujeme šachy. Součástí takové hry bude jistě
    i komponenta, která pro daný stav šachovnice a vybranou figurku
    vrátí seznam pozic na šachovnici, kam lze s figurkou táhnout.

    Seznam pozic musí vzít v potaz barvy figurek, jejich sbírání apod.
"""

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

tile = (6, 3)

# chceme vytisknout pozice (5, 3) a (4, 3)

# jak budeme šachovnici reprezentovat?
# chceme ji umět načíst a vytisknout - to jsou první dva úkoly
