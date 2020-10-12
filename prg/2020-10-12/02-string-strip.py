"""
    Implementujte program, který se chová jako .strip() funkce
    na řetězcích. Tedy zahodí z řetězce mezery před a za.

    Př.:

        "  ahoj svete    " --> "ahoj svete"
        "ahoj svete    "   --> "ahoj svete"
        "  ahoj svete"     --> "ahoj svete"
        "ahoj svete"       --> "ahoj svete"

    Vstup načte pomocí input() a výsledek vytiskne společně se dvěmi
    šipkami, aby bylo poznat že tam opravdu žádné mezery nejsou:
        
        print(">" + vysledek + "<")
"""

given_string = "   ahoj svete   "

start_index = 0
while given_string[start_index] == " ":
    start_index += 1

end_index = -1
while given_string[end_index] == " ":
    end_index -= 1

print(">" + given_string[start_index:(end_index + 1)] + "<")

# Tohle je procedurální řešení (tzn. používá konrétní instrukce
# co se má jak udělat, pamatujeme si nějaké indexy, máme cykly).
# 
# Lze ale použít víc funkcionální řešení, které pracuje s abstraktnějšími
# objekty. Například můžeme rozthat vstup na slova (.split()) a potom
# ho zase slepit se znakem mezery:
#
#   " ".join(given_string.split())
#   # (což teda nedělá přesně to samé, ale je to spíš jen jako příklad)
#
# Hmm, co si z toho má vzít?
# Že je dobré znát tyhle pomocné metody jako je .strip(), .split(), .join(),
# ale že bych měl i chápat, jak jsou vevnitř implementované.
