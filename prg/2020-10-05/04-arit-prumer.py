# Uživatel zadává čísla, dokud nezadá prázný vstup (enter).
# My pak vypíšeme aritmetický průměr zadaných čísel.
#
# 5
# 8
# 4
# 9
#
# Arit průměr je: xxx

finished = False
total_sum = 0
total_count = 0

while not finished:
    x = input()
    
    if x == "":
        finished = True
    else:
        total_sum += float(x)
        total_count += 1

print("Celkový součet je: " + str(total_sum))
print("Celkový počet je: " + str(total_count))
print("Arit. prumer: " + str(total_sum / total_count))

# Ctrl + C na zabití programu !