# Eukleidův algoritmus

Implementujte Eukleidův algoritmus.

Program dostane na vstupu dvě celá kladná čísla na jednom řádku. Na výstup vypíše postup algoritmu až do posledního kroku a poté vypíše nejmenšího společného dělitele obou zadaných čísel.

Tedy pro vstup:

```
142 1024
```

Program vypíše:

```
1024 142
142 30
30 22
22 8
8 6
6 2
2
```

Na každém řádku výstupu je jeden krok algoritmu. První řádek odpovídá číslům na vstupu. Každý řádek má vlevo to větší z obou čísel. Jedním krokem se rozumí dělení se zbytkem, ne odečítání. Poslední vypsaný krok je ten, kdy zbytek po dělení vyjde `0`. Poté následuje hodnota nejmenšího společného dělitele.
