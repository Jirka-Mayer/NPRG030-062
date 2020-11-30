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
    - eukleidův algoritmus

**Programování**

- googlit
- git
- list comprehension
    - plyne z matematické definice množin
    - map, filter
- příklady - pohyb šachových figurek
    - 1) reprezentace šachovnice
        - funkce strčíme do souboru board.py
    - 2) tisk šachovnice společně se seznamem červených políček
    - 3) pěšák rovně
        - funkce strčíme do souboru piece.py
    - 4) král
    - 5) věž
- zadej dcv
    - Game of life


## Plán na 2020-10-26

**Algoritmizace**

- příklady
    1) implementuj binární vyhledávání nad polem
        - vygeneruj pole náhodných čísel a setřiď ho (sort())
        - implementuj binární vyhledávání
    2) implementuj zásobník - třída `Stack`
        - proč? Nestačí list?
            Omezení API + zachování invariantů (např. nelze přehodit prvky)
            Pro 90% použití stačí list.
        - print
            - `__repr__(self)`
        - privátní metody / proměnné
        - push, pop
        - peek
- zadej dcv
    - hledání vadné kuličky


**Programování**

- příklady
    1) validní řetězec závorek - "()((()())())" vs "((()(", "()(()))"
        - vymysleme algoritmus dohromady
        - využij zásobník z algoritmizace
        - implementuje každý sám
- přednáška
    2) načítání a ukládání textu v souboru
        - Příklad - načti soubor a převeď řádky na uppercase s uvozovkama
        - otevření, zavření souboru `r`
            - `with` - nezapomenete soubor zavřít
        - čtení řádek po řádku
        - zápis do souboru `w`, vytvoří/vymaže soubor
        - append na konec souboru `a`
        - přečtení všech řádek naráz
        https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
- příklady
    3) zobrazení obrázku PBM
        - https://cgg.mff.cuni.cz/~pepca/lectures/pdf/icg-06-rasterformats.pdf
        - https://en.wikipedia.org/wiki/Netpbm
- zadej dcv
    - skalární součin vektorů


## Plán na 2020-11-02

**Algoritmizace**

- páté cvičení
- příklady
    1) naprogramujeme si haldu
    https://dl1.cuni.cz/pluginfile.php/1081151/mod_resource/content/5/3%20Trideni.pdf
- zadej dcv
    - Hledání vadné koule pro N koulí, vyjádři "časovou složitost" v O notaci


**Programování**

- přednáška
    - standardní vstup
        BASH>  ./program < input.txt > output.txt
        PS>    Get-Content input.txt | ./program > output.txt
- příklady
    1) zobrazení obrázku PBM
        - https://cgg.mff.cuni.cz/~pepca/lectures/pdf/icg-06-rasterformats.pdf
        - https://en.wikipedia.org/wiki/Netpbm
    2) když zbyde čas, tak RLE kompresi obrázku
- zadej dcv
    - váhy - implementace


## Plán na 2020-11-09

**Algoritmizace**

- šesté cvičení
- pozn: FEEP nebyl na windows vidět
- pozn: dnes je poslední den na váhy, budou třeba na další 2 úkoly
- příklady
    1) implementace merge sort
    2) rekurze je cool, šla by použít na posčítání seznamu?
        - pozor na stack overflow
- zadej dcv
    - dokončit haldu z minula a implementovat heapsort


**Programování**

- příklady
    - sokoban
        - https://en.wikipedia.org/wiki/Sokoban
        - zeď `##`, box `[]`, hráč `:)`, cíl `--`, cíl s boxem, `{}`
        - rozmyšlení vstupu, výstupu, architektury
        - rozdělení na části
        - reprezentace světa, hráče, krabic, cílových políček
- zadej dcv
    - bases, od Holana


## Plán na 2020-11-16

**Algoritmizace**

- sedmé cvičení
- bucket sort
    - setřídíme tisíc lidí podle jejich věku
- implementace fronty pomocí spojového seznamu
- dcv: (libovolná) implementace prioritní fronty


**Programování**

- povídání o zápočtových programech
- run-length encoding souborů .pgm (nebo obecně souborů s čísly oddělenými mezerami)
- dcv: skoro-setřízená posloupnost


## Plán na 2020-11-23

**Algoritmizace**

- osmé cvičení
- rekurze:
- počet zápisů čísla jako součtů posloupnosti přirozených čísel
    - nejprve rozmyslet (ať píšou na tabuli) + rekurze ??
    - implementovat pro počty
    - nejen počet, ale je i vypsat (jen zmínit, ne programovat)
    - cachování
    - počet různých rostoucích posloupností
- dcv - vypsat všechny permutace pro dané N


**Programování**

- pygame, základy kvůli zápočťákům
    - https://www.pygame.org/wiki/GettingStarted
    - instalace - přes python z terminálu
- 01-pygame.py - projít, popsat
- 00-pygame-template.py - projít
- 02-board.py ... zadat, naprogramovat
- zmínit numpy, opencv, matplotlib
- dcv - tři poskakující koule


## Plán na 2020-11-30

**Algoritmizace**

- deváté cvičení
- počet zápisů čísla jako součtů posloupnosti přirozených čísel
    - zopakovat co bylo minule, zasekli jsme se na tom, že jsme některé výrazy počítali několikrát
        - proč několikrát? Co jsme reálně počítali? (stromy)
    - co jsme chtěli počítat - posloupnosti, řešení zkracováním o 1 prvek
        - stromy -> půlení (binární); posloupnosti -> zkracování o 1
    - příklady nejprve společně vymyslet a teprve potom implementovat:
    - příklad: vypište všechny posloupnosti "+--++-+-+" délky N
    - POČÍTÁNÍ VS. VYPISOVÁNÍ
    - Generátory
    - MEMOIZACE!
    - příklad: kolik existuje binárních stromů na N vrcholech? (Katalánova čísla)
        - vztah mezi počtem listů úplného bin. stromu a počtem vnitřních vrcholů
        - https://en.wikipedia.org/wiki/Catalan_number
- dcv - vypiš všechna platná uzávorkování pro N otevíracích a N zavíracích závorek


**Programování**

- organizace projektu
- přetěžování operátorů
- dcv - P1M: Třída na obdélníky


## Plán na 2020-12-6

**Algoritmizace**

- desáté cvičení
- ...


**Programování**

- RLE dekomprese
- nová šablona na pygame
- pálení papíru (v pygame na Surface)


## Nápady do budoucna

- Do příště: radši menší příklady a dávat na ně víc času, aby to lidi stihli programovat

- RLE dekomprese
- pálení papíru (kasiopea), naivně, pomocí fronty
- testování - jak ověřit funkčnost programu? Testovací data, automatické testy
- matice - implementovat třídu Matrix
- trije a radix sort
- flood fill pomocí fronty
    - nejprve nastavíme jeden pixel
- parsovat a vyhodnocovat prefixovou notaci - výrazy: `*(+(1,5),8)`
- FEEP
    - negativ obrázku - `compute_negative().draw()`, vyrobí novou instance `PgmImage`
- přepsat sokobana do pygame - proč je důležitý dobrý návrh
