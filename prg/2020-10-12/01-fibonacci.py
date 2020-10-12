"""
    Vypiš prvích N čísel z Fibonacciho posloupnosti:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34     (pro N = 10)
    (stačí vypsat na řádky pod sebou, nemusí být takhle za sebou)

    První dvě čísla jsou 0 a 1, každé další je součet dvou předchozích.
"""

N = int(input())

# INVARIANT: "a" je předposlední a "b" je poslední
a = 0
b = 1
print(a)
print(b)

for i in range(N - 2):
    # napočítej novej stav programu
    new_a = b
    new_b = a + b

    # vytiskni to další číslo v posloupnosti
    print(new_b)

    # oprav invariant
    a = new_a
    b = new_b
