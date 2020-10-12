"""
    Přihrádkově setřiď data od nejmenších.
    (zkoppíruj kód z předchozí úlohy a uprav)

    Chci proměnnou `sortedData`, která bude obsahovat seznam `data`,
    ale setřízenou.

    Zamysli se nad časovou složitostí. Není nějaká super dobrá?
"""

data = [
    9, 7, 8, 9, 0, 6, 2, 0, 8, 4, 5, 2, 9, 7, 2, 8, 9, 1, 5, 2,
    1, 6, 0, 1, 7, 7, 9, 1, 1, 9, 4, 5, 3, 5, 0, 0, 7, 7, 4, 7,
    9, 5, 1, 5, 2, 6, 1, 3, 3, 8, 6, 1, 9, 9, 9, 6, 8, 1, 9, 1,
    3, 7, 6, 8, 3, 5, 5, 3, 8, 3, 3, 2, 9, 6, 7, 4, 6, 7, 0, 1,
    0, 4, 9, 5, 2, 9, 5, 0, 6, 7, 5, 2, 7, 7, 6, 9, 8, 5, 3, 5
]

# počítání výskytů

digit_counts = [0] * 10

for d in data:
    digit_counts[d] += 1


# třídění

sorted_data = []
for i in range(10):
    sorted_data += [i] * digit_counts[i]

print(sorted_data)

# nebylo na cviku:
# můžu setřídit data na místě, čímž ušetřím nějaké alokace
# a triky s [i] * 123, apod:
# (takhle bych to implementoval mimo python)

at = 0
for digit in range(10):
    for i in range(digit_counts[digit]):
        data[at] = digit
        at += 1

print(data)
