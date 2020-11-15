import random


def random_syllable():
    vowel = "aeiouy"
    consonant = "bcdfghjklmnpqrstvwxz"
    
    syllable = random.choice(vowel)
    if random.random() > 0.5:
        syllable += random.choice(consonant)
    if random.random() > 0.5:
        syllable = random.choice(consonant) + syllable
    return syllable


def random_name():
    return "".join([random_syllable() for _ in range(random.randint(1, 3))])
