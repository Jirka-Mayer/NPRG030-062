"""

Epizoda II: Součty útočí
------------------------

Napište program, který pro dané N vypíše všechny různé posloupnosti přirozených čísel,
jejichž součet je právě N.

Tzn pro N = 3 jsou to posloupnosti:
    1 + 1 + 1
    1 + 2
    2 + 1
    3
"""

cache = {}

def K(N):
    global cache

    if N == 0:
        return 1

    if N in cache:
        return cache[N]
    
    total = 0
    for i in range(N):
        total += K(i)
    
    cache[N] = total
    return total


for i in range(1000):
    print(i, K(i))
