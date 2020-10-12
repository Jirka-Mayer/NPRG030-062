"""
    Načítej čísla ze vstupu, dokud uživatel nezadá prázný vstup.
    Potom všechna zadaná čísla vypiš v opačném pořadí.
"""

numbers = []

# načíst vstup od uživatele
while True:
    given_string = input()

    if given_string == "":
        break # vyskoč z cyklu ven
        
        # ještě tu máme 'continue', který skočí na začátek cyklu
        # (a znovu kontroluje podmínku cyklu)
    
    numbers.append(int(given_string))
    
# vypiš v opačném pořadí
#
# používáme koncept "zásobníku" s operacemi "push" a "pop"
#   jenže python má míst .push metodu .append
#   pop je opak appendu - vrátí poslední prvek a z listu ho smaže
while len(numbers) > 0:
    print(numbers.pop())
