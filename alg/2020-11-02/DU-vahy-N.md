# Váhy - pro N koulí

Úloha navazuje na úlohu **Váhy**.

**Backstory:** Máme 7 zlatých kuliček, jedna je vadná (je lehčí), chceme ji nalézt na co nejméně vážení. Máme rovnoramenné váhy, na miskách vah může být neomezený počet kuliček, váhy dokážou určit rovnost.

Vymyslete postup, který minimalizuje počet vážení pro libovolný počet koulí (`N`). (třeba 65 tisíc koulí) Jak bychom měli koule dávat na misky, abychom použili vážení co nejméně? Překdpokládáme, že na misky vah se vejde neomezený počet koulí.

Poté co algoritmus vymyslíte, tak určete jeho časovou složitost v `O()` notaci. Časovou složitostí mám na mysli počet provedených vážení. Jak zavísí na `N`?

Příklad naivního algoritmu by bylo: "Budu vážit postupně všechny dvojice, až dokud nenarazím na vadnou kouli". Takový algoritmus provede zhruba `N / 2` vážení, takže jeho časová složitost bude `O(N)`.
