# Prioritní fronta

Implementujte prioritní frontu. Jedná se běžnou frontu s operacemi *enqueue* a *dequeue*, která ale navíc má pro každý prvek nějaké skóre a během volání *dequeue* se vrátí prvek s nejvyšším skóre (nebo první vložený z více prvků s maximálním skóre).

Program dostane na vstupu posloupnost příkazů pro frontu:

```
ENQUEUE a 5
ENQUEUE b 9
DEQUEUE
ENQUEUE c 12
DEQUEUE
DEQUEUE
DONE
```

Příkazy odpovídají operacím na frontě:

- `ENQUEUE` vloží prvek do fronty s daným jménem a celočíselným skóre.
- `DEQUEUE` odebere prvek na začátku fronty a vytiskne ho na výstup (viz níže).
- `DONE` je poslední příkaz po kterém program může skončit.

Výstup programu pro vstup nahoře bude tedy následující:

```
b 9
c 12
a 5
```

Máte zajištěné, že dequeue se nebude volat na prázdné frontě, že název prvku neobsahuje znak mezery a že skóre jsou celočíselná.
