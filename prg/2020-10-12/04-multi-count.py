"""
    Máme nějaká data (viz. níže), chceme je projít a spočítat
    frekvenční tabulku (kolikrát se které číslo vyskytlo v datech).
    Čísla v datech jsou pouze v rozmezí 0 až 9.

    Správné počty (pro kontrolu) jsou:
        0: 8x            5: 13x
        1: 11x           6: 10x
        2: 8x            7: 13x
        3: 9x            8: 8x
        4: 5x            9: 15x
"""

data = [
    9, 7, 8, 9, 0, 6, 2, 0, 8, 4, 5, 2, 9, 7, 2, 8, 9, 1, 5, 2,
    1, 6, 0, 1, 7, 7, 9, 1, 1, 9, 4, 5, 3, 5, 0, 0, 7, 7, 4, 7,
    9, 5, 1, 5, 2, 6, 1, 3, 3, 8, 6, 1, 9, 9, 9, 6, 8, 1, 9, 1,
    3, 7, 6, 8, 3, 5, 5, 3, 8, 3, 3, 2, 9, 6, 7, 4, 6, 7, 0, 1,
    0, 4, 9, 5, 2, 9, 5, 0, 6, 7, 5, 2, 7, 7, 6, 9, 8, 5, 3, 5
]

# ===========
# zadávání vlastního vstupu na jeden řádek
# (odkomentuj, pro použití)

# given_input = input()
# data = []
# for i in given_input.split():
#     data.append(int(i))

# ===========

digit_counts = [0] * 10

for d in data:
    digit_counts[d] += 1

for i in range(10):
    print(str(i) + ":", str(digit_counts[i]) + "x")
