"""
Napište program, který zobrazí v konzoli obrázek formátu PGM.

Viz. soubor "feep.pgm":
- první řádek je formát souboru "P2", určuje jak vypadá zbytek
- další řádek jsou rozměry - šířka výška
- další řádek je maximální hodnota (co je bílá), černá je vždy 0
- poté následuje jeden řádek pro každý řádek obrázku

Vyrobte si třídu PgmImage, která bude obrázek reprezentovat
"""

import os


def print_pixel(intensity):
    """Vytiskne jeden šedotónový pixel s intenzitou mezi 0.0 a 1.0"""
    black = 232
    white = 255
    code = black + int(intensity * (white - black))
    print("\33[48;5;" + str(code) + "m  \33[0m", end="")


class PgmImage():
    def __init__(self, file_name):
        self.__pixels = []
        self.__width = 0
        self.__height = 0
        
        self.__load_from_file(file_name)

    def __load_from_file(self, file_name):
        abs_path = os.path.dirname(os.path.realpath(__file__)) + "/" + file_name
        with open(abs_path, "r") as f:
            assert f.readline() == "P2\n"
            
            # load dimensions
            self.__width, self.__height = f.readline().split()
            self.__width = int(self.__width)
            self.__height = int(self.__height)

            # load color depth
            white_value = int(f.readline())
            
            # reset pixel list
            self.__pixels = []

            # load all rows
            for _ in range(self.__height):
                row = self.__load_row(f, white_value)
                assert len(row) == self.__width
                self.__pixels.append(row)

    def __load_row(self, f, white_value):
        string_pixels = f.readline().split()
        int_pixels = [int(p) for p in string_pixels]
        float_pixels = [p / white_value for p in int_pixels]
        return float_pixels

    def draw(self):
        for row in self.__pixels:
            for pixel in row:
                print_pixel(pixel)
            print()


def main():
    img = PgmImage("feep.pgm")
    img.draw()


main()
