ball_count = 3
target_ball = 2
max_weigh_count = 1

weigh_count = 0

def get_balls():
    """Vrátí list všech koulí"""
    global ball_count
    return list(range(ball_count))

def weigh(left, right):
    """
        Zváží pravou a levou stranu a řekne, která strana je lehčí (která stoupne),
        resp. která strana vah obsahuje vadnou kouli.
        Funkce tedy vrátí "left", "right", nebo "same".
        Pokud se váhy rozbijí opotřebením, vyhodí se výjimka, která zabije program.
    """
    global weigh_count, max_weigh_count, ball_count, target_ball

    # ošetření vstupu
    assert type(left) is list, "Na levé straně vah není list, ale " + repr(type(left))
    assert type(right) is list, "Na pravé straně vah není list, ale " + repr(type(right))
    assert all([(type(b) is int and b >= 0 and b < ball_count) for b in left]), \
        "Levá strana obsahuje neexistující koule: " + repr(left)
    assert all([(type(b) is int and b >= 0 and b < ball_count) for b in right]), \
        "Pravá strana obsahuje neexistující koule: " + repr(right)

    # opotřebení vah
    weigh_count += 1
    if weigh_count > max_weigh_count:
        raise Exception("Váhy se rozbily!")
    
    # různý počet koulí, takže se váhy pohnou vždy a jsou k ničemu
    if len(left) > len(right):
        return "right"
    elif len(left) < len(right):
        return "left"

    # vážení při stejném počtu koulí
    if target_ball in left:
        return "left"
    elif target_ball in right:
        return "right"
    else:
        return "same"
