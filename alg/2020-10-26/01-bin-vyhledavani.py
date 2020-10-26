"""
Vygeneruj pole o 50 prvcích (celá čísla mezi 0 a 100),
setřiď ho a binárně v něm vyhledej, na které pozici je
(nebo by mělo být) číslo 42.
"""

import random

random.seed(5)

data = [random.randint(0, 100) for _ in range(50)]
data.sort()

# =====================

subject = 94

bottom = -1
top = len(data)

print(data)

while True:
    print(top, bottom)
    
    if top == bottom + 1:
        print("Prvek tam není, ale byl by nad:", bottom)
        exit()

    middle = (bottom + top) // 2
    if data[middle] == subject:
        print("Máme ho, na pozici:", middle)
        exit()
    elif data[middle] > subject:
        top = middle
    else:
        bottom = middle
