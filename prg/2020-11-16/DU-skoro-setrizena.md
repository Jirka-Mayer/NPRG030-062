# Skoro setřízená

**Def:** Řekneme, že posloupnost je skoro-setřízená, pokud nějaká její rotace je setřízená (vzestupně).

**Def:** Rotace posloupnosti, je libovolné "posunutí" prvků posloupnosti s tím, že prvky přepadávající na jednom okraji se objeví na opačném okraji. Například posloupnost `a b c d` můžeme rotovat doprava o jeden prvek a dostaneme `d a b c`. Stejně tak ji můžeme rotovat o dva prvky a dostaneme `c d a b`.

Napište program, který dostane posloupnost celých čísel a má určit, zda se jedná o skoro-setřízenou posloupnost či nikoliv.

Standartní vstup může vypadat např. takto:

```
12 18 25 3 7
```

Odpovídající výstup bude:

```
True
```

Protože se jedná o skoro-setřízenou posloupnost. Rotací doprava o dva prvky dostaneme `3 7 12 18 25`.
