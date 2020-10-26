"""
Jak načítat a zapisovat soubory?

Použij soubory "example.txt" a "output.txt"
"""

# ČTENÍ ======================================

# získání absolutní cesty
import os

example_file_path = os.path.dirname(os.path.realpath(__file__)) + "/example.txt"
output_file_path = os.path.dirname(os.path.realpath(__file__)) + "/output.txt"

# přečtu první řádek souboru
f = open(example_file_path, "r")
print(repr(f.readline()))
f.close()

# přečtu první řádek, ale s "with"
with open(example_file_path, "r") as f:
    print(repr(f.readline()))

# přečtu všechny řádky do pole
with open(example_file_path, "r") as f:
    print(repr(f.readlines()))

# přečtu všechny řádky postupně, ručně
with open(example_file_path, "r") as f:
    while True:
        line = f.readline()

        if line == "":
            break

        print(repr(line))

# přečtu všechny řádky postupně, for
with open(example_file_path, "r") as f:
    for line in f:
        print(repr(line))


# ZÁPIS ======================================

# zapíšu kus textu (vymaž nebo vytvoř soubor)
with open(output_file_path, "w") as f:
    f.write("ahoj")

# zapíšu řádek
with open(output_file_path, "w") as f:
    f.write("první řádek\n")
    f.write("druhý řádek!\n")

# přidání na konec (nebo vytvoř)
with open(output_file_path, "a") as f:
    f.write("první řádek\n")
    f.write("druhý řádek!\n")
