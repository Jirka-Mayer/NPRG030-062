"""
Kolik existuje binárních stromů na N vrcholech?
Vyřeš rekurzivně.

Řešení:
Strom o N vrcholech je 1 kořen a dva podstromy. Podstromy mohou být velikosti 0 až N - 1,
ale v součtu musí mít velikost N - 1. Čili podstromy jsou velikostí:
0 a (N-1)
1 a (N-2)
...
(N-1) a 0
"""

def C(N):
    if N == 0:
        return 1
    
    if N == 1:
        return 1
    
    total = 0
    
    for i in range(0, N):
        total += C(i) * C(N - 1 - i)

    return total


for N in range(10):
    print(C(N))
