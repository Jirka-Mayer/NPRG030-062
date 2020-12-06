# Intervaly

Vypište všechny celočíselné intervaly, které existují mezi čísly `0` a `N`.

Tedy pro `N = 3` jsou to intervaly:

```
0 1
0 2
0 3
1 2
1 3
2 3
```

Hodnotu `N` načtete ze standardního vstupu (`input()`) a seznam intervalů vypíšete v libolovném pořadí na výstup, jeden interval na řádek jako dvě čísla oddělená mezerou.

Pro kontrolu můžete intervaly spočítat a mělo by jich být právě tolik:

```
print(sum(range(1, N + 1)))
```

Můžete zkusit použít generátory (`yield`), představené na minulém cvičení.
