"""
Napište program, který zobrazí v konzoli obrázek formátu PGM.

Viz. soubor "feep.pgm":
- první řádek je formát souboru "P2", určuje jak vypadá zbytek
- další řádek jsou rozměry - šířka výška
- další řádek je maximální hodnota (co je bílá), černá je vždy 0
- poté následuje jeden řádek pro každý řádek obrázku

Vyrobte si třídu PgmImage, která bude obrázek reprezentovat
"""


def print_pixel(intensity):
    """Vytiskne jeden šedotónový pixel s intenzitou mezi 0.0 a 1.0"""
    black = 232
    white = 255
    code = black + int(intensity * (white - black))
    print("\33[48;5;" + str(code) + "m  \33[0m", end="")


def main():
    # dummy: vytiskne spektrum
    for i in range(20 + 1):
        print_pixel(i / 20)
    print()


main()
