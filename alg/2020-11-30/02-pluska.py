"""
Vypište (rekurzivně) všechny posloupnosti znaků "+" a "-" délky N.

Tedy pro N = 3 to jsou:
    ---
    --+
    -+-
    -++
    atd...
"""

def f(N):
    if N == 1:
        return ["+", "-"]

    seqs = []

    for sub_seq in f(N - 1):
        seqs.append("+" + sub_seq)
        seqs.append("-" + sub_seq)

    return seqs


for s in f(4):
    print(s)
