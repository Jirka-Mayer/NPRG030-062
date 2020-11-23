"""
Napište program, který pro dané N napíše počet různých posloupností přirozených čísel,
jejichž součet je právě N.

Tzn pro N = 3 jsou to posloupnosti
    1 + 1 + 1
    1 + 2
    2 + 1
    3
tedy program vrátí "4".
"""

def sequences(N):
    if N == 1:
        return [[1]]

    out = []

    out.append([N])

    for i in range(1, N):
        left = sequences(i)
        right = sequences(N - i)

        for l in left:
            for r in right:
                out.append(l + r)

    return out


def stringify(sequences):
    return ["+".join([str(x) for x in s]) for s in sequences]


# MAIN

s = stringify(sequences(10))
print(len(s))
print(len(set(s)))
