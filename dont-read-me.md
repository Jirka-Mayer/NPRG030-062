# Poznámky cvičícího

Algorimizace - Dingle:
https://ksvi.mff.cuni.cz/~dingle/2019/algs/intro_to_algorithms.html

Programko ještě v pascalu:
https://www.ms.mff.cuni.cz/~dvoram30/prg1ct/aktuality.html

Programko - Rudolf Rosa:
https://ufal.mff.cuni.cz/courses/nprg030

Programko - Dingle:
https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/programming_1.html

Tomáš Souček - příklady z algoritmizace:
https://github.com/soCzech/teaching/tree/master/2021winter

Rudolf Kryl 2009
https://ksvi.mff.cuni.cz/~kryl/Avyuka/200910/infCv46.html


## Plán na 2020-10-05

**Algoritmizace**

> Chtěl bych řešit úlohy typu ADS, kombinatorické hry apod.

- zmínit nahrávání, začít nahrávat
- tykání
- organizační věci
    - tenhle repozitář - projdi poznámky
- řešíme úlohy
    1) najdi největší prvek v poli (jeho hodnotu)
        - N prvků, chceme to na (N - 1) porovnání
        - naivní N^2
        - lineárně / rekurzivně?
        - paměť? stream? distribuovanost?
    2) najdi daný prvek v setřízeném poli (jeho hodnotu)
        - naivně, binárně
        - rezeber složitosti
    3) najdi pozice všech největších prvků v náhodném poli
        - jeden průchod? Dva průchody? Co na to čas a paměť?
    4) Kuličky
        V nádobě je N kuliček. Kuličky jsou černé a bílé. Kuličky budu z nádoby
        odebírat následujícím způsobem: Vytáhnu dvě a místo nich jednu jinou vrátím do nádoby:
            `Bílá + Bílá --> Bílá`
            `Černá + Bílá --> Černá`
            `Černá + Černá --> Bílá`
        Jakou barvu bude mít poslední kulička co v nádobě zbyde?
    5) Cesta věží na šachovnici
        Máme šachovnici `8 x 8` a jedno startovní políčko. Hledáme cestu věží ze startovního políčka, která projde všemi políčky šachovnice právě jednou a je "uzavřená" (skončí na sousedním políčku startovního políčka)
            - a co když odebereme roh?
- zadat úkol
    - Lámání čokolády
        Máme tabulku čokoládu o `M x N` dílcích. Jaký je nejmenší počet rozlomení
        čokolády, abychom od sebe oddělili všechny dílky? Vždy smíme lámat pouze jeden kus čokolády (nelze lámat více vrstev na sobě).

**Programování**

> Chtěl bych programovat v pythonu spíš jednodušší věci. Kódit.

- organizační věci
    - tenhle repozitář - projdi poznámky
- chci procvičit věci z přednášky, abyste je nemuseli (tolik) cvičit doma
- programujme příklady
    - googli, ale nekopíruj, pochop a opiš (taky pozor tabs & spaces)
    1) sečti dvě zadaná čísla
    2) zadej věk, je víc než 18?
    3) automat - rozskok na 3 možnosti (Káva, Čaj, Exit)
    4) aritmetický průměr zadaných čísel, stopka je `""`
        - pobavit se o časové a paměťové složitosti
        - co tak si čísla pamatovat? Ukaž pole
    5) vypiš právě 10x `Hello world!`
        - ukaž for loop
        - ukaž pro předchozí problém s polem
    6) vypiš prvních 10 Fibonacciho čísel
- zadat úkol
    - Hvězdičky


## Plán na 2020-10-12

**Algoritmizace**

- domácí úkol
    - Není tam nějaký invariant?
    - Nejde dát do vztahu počet kusů čokolády a počet provedených zlomení?
- eukleidův algoritmus
- pište řešení do google drive souboru
- příklady
    1) Velbloud
    2) Sklenice
    3) Mince na stole
- zadat úkol
    - Kamínky na pásce - kombinatorická hra

**Programování**

- googli, ale nekopíruj, pochop a opiš (taky pozor tabs & spaces)
    - jak se zjistí délka seznamu?
    - jak se přidá prvek na konec seznamu?
- zkopírujte řešení do google drive souboru
- příklady
    1) vypiš prvních 10 Fibonacciho čísel
    2) string strip (trim) - ořízni zadaný text
    3) vypiš zadaná čísla v opačném pořadí
        - jak roztrhnout čísla na jedné řádce? `.split()`
        - zásobník
        - `[::-1]`
    4) spočítej počty výskytů jednotlivých čísel ve vstupu (omezené rozmezí čísel)
    5) přihrádkové třídění
-zadat úkol
    - Počet slov ve větě


## Plán na 2020-10-19

**Algoritmizace**

- eukleidův algoritmus
- příklady
    1) Mince na stole
- zadej dcv
    - TODO

**Programování**

- příklady
    - TODO
- zadej dcv
    - TODO