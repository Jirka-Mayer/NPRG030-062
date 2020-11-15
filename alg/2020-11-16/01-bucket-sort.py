"""
Implementujte přihrádkové třídění lidí podle jejich věku.
Lidé mají věk v rozmení 0 - 100 včetně a je jich 1 000
"""

import random
from random_name import random_name


def random_age():
    return random.randint(0, 100)


# generate the input data
random.seed(5)
people = [
    (random_name(), random_age())
    for _ in range(1000)
]

# TODO: implement the sort
sorted_people = people

# print out the result
for person in sorted_people:
    print(repr(person).rjust(20))
