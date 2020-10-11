# Kameny na pásce

Dva hráči hrají následující deskovou hru. Hracím plánem je jedna páska tvořená 1000 políčky, pole jsou očíslována zleva doprava přirozenými čísly od 1 do 1000. Na začátku hry na náhodně zvolených dvou různých polích leží hrací kameny. Výchozí situaci hry lze tedy popsat dvojicí různých celých čísel od 1 do 1000. Oba hráči se ve hře pravidelně střídají. Hráč, který je na tahu, zvolí jeden z kamenů a přemístí ho o libovolný počet polí směrem doleva. Musí přitom kámen posunout alespoň o jedno políčko a zároveň svým tahem nesmí přeskočit jiný hrací kámen ani nesmí umístit přesouvaný kámen na již obsazené políčko. (Tah tedy nelze provést s kamenem stojícím na políčku číslo 1 ani s kamenem stojícím na políčku `i`, je-li políčko číslo `i - 1` právě obsazené.) Hra končí ve chvíli, kdy už nelze provést žádný tah, tzn. až se dostanou oba hrací kameny na políčka s čísly 1 a 2. Zvítězil ten z hráčů, který svým tahem dosáhl této koncové situace. **Určete, jaké pozice jsou vyhrané a jaké prohrané.**

**Jinými slovy:** Právě jste na tahu a koukáte na pásku. Vymyslete strategii, jak zaručeně vyhrát (což ne v každé situaci lze). Ve kterých situacích umíte zaručeně vyhrát a ve kterých prohrajete? (pokud protihráč neudělá chybu)

```
  1   2   3   4   5   6   7
+---+---+---+---+---+---+---+--
|   |   |   | o |   | o |   | ...
+---+---+---+---+---+---+---+--

Tohle je pozice [4, 6]
```