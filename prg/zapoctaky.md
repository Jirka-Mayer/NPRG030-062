# Zápočťáky

- chci od každého téma do konce listopadu
    - tzn. chci aby mi každý poslal (resp. jsme se dohodli na) *specifikaci zápočtového programu*
    - specifikací se rozumí stručný popis toho, co by váš program měl dělat
    - specifikace je to, co rozhodne, jestli jste napsali program, který se po vás chtěl, nebo ne
    - specifikace by měla obsahovat radši méně věcí. Lepší nakonec dodat víc než bylo slíbeno, než nedodat něco co mělo být dodáno.
    - Např.: "Implementuji hru carcassonne v prostředí pygame. Hra bude pro dva a více živých hráčů, tzn. nebude obsahovat umělou inteligenci. Detailní pravidla hry jsou na adrese -url-."
    - Např.: "Implementuji first-person-shooter controller jako skript pro herní engine Unity. Kontroler by měl umožňovat pohyb po libolné sadě colliderů z 3D fyzikálního systému Unity, měl by umožnit skákání a narážení hlavou do stropu. Měl by spolehlivě detekovat stání na zemi (tzn. při chůzi zkopce nebude tvrdit, že se znáší). Hráč by neměl být schopen zatočit ve vzduchu."
- dva lidé nesmí mít to samé (kdo dřív přijde...)
- neměla by to být knihovna, ale program. Lze udělat knihovnu a pak ji použít v ukázkové aplikaci
- radši méně kódu, ale hezky strukturovaného a čitelného
    - tzn. není třeba databáze s dvaceti datovými typy. Stačí dva typy, ale mít pěknou strukturu kódu pro monžné rozšíření
- program by měl být rozumně odlazený (abych při vyzkoušení nenarazil na bugy, ale rozhodně bych neměl být jako uživatel schopný program shodit, když nedělám nic úchylného)
- dokumentace (https://ksvi.mff.cuni.cz/~kryl/dokumentace.htm)
    - uživatelská = vysvětlete někomu kdo není programátor, jak se váš program používá
        - Např.: Program čte vstup ze souboru `input.csv` a ten má takový a takový formát. Program má 3 argumenty na příkazové řádce a ty ovlivňují následující... V případě chyby program vygeneruje soubor `error.log`...
        - Např.: Kliknutím a tažením RMB můžete posouvat kameru po světě, kolečkem přibližujete. Dvojklik zobrazí detail komponenty...
        - Např.: Server běží v prostředí node.js, takže pro jeho spuštění budete muset mít nainstalovaný node. Spuštění z příkazové řádky provedete příkazem: ...
    - vývojová = vysvětlete mně (nebo vašemu spolužákovi) hlavní strukturu a koncepty vašeho programu, aby ho pochopil do takové míry, že bude schopný program rozšířit, případně bude vedět kde v kódu hledat, kdyby měl opravovat nějakou chybu (tady se vám bude rozhodně ušetří práci to, že budete mít přehledný kód)
        - Např.: Program dělá diskrétní simulaci světa, svět je mřížka buňěk, buňky jsou ty a ty. Program žije ve třídě `Program` a používá třídy `World`, `SimulationPolicy` a `EvolutionRecorder` jako hlavní komponenty celé aplikace. ...
- osobní předvedení programu (není povinné, ale doporučuji - nebudeme muset řešit všechno přes email)


## Co by se dalo dělat?

Od Martina Mareše: http://mj.ucw.cz/vyuka/zap/

Osobně doporučuji něco, o čem se budete učit později na MFF. Zabijete tím dvě mouchy jednou ranou a ušetříte si tak práci s učením v budoucnu. I když se jedná o něco, co teď neumíte - můžete se to naučit a proto já schválím, jestli je složitost programu adekvátní, nebo jste si naložili příliž.

Průvodce labyrintem algoritmů: http://pruvodce.ucw.cz/

- grafy
    - hledání nejkratší cesty: dijkstra, A*
    - hledání maximálního toku v tokové síti
    - hledání cyklů
    - hledání komponent souvislosti
- text
    - Aho-Corrasick
    - Knuth-Morris-Pratt
    - regulární výrazy
    - překladače, kompilátory, interpretery, pretty-printery, lintery, transpilery
    - zpracování přirozeného jazyka
        - překladač
        - určování pádu, sklnování slov
        - generování textu pohle šablony (překladové systémy pro softwarové vývojáře)
            - `"There were :bug_count: #bug(s) in your program."`
- geometrické problémy
    - triangulace polygonů
    - binární operace na tělesech
    - zpracování obrazu / volumetrických dat (minecraft?)
- kombinatorické hry (šachy, piškvorky, ...)
    - prohledávání stavového prostoru
    - prořezávání
    - heuristky
- automaty a gramatiky
    - konečné deterministické automaty vs. regulární výrazy vs. nedeterministické
    - simulace turingova stroje
    - compiler pro turingův stroj (assembler -> turing)
    - busy beaver
- hardwarové věci
    - simulace hradel
    - simulace jednoduchých starých procesorů nebo podmnožin procesorů (např. MIPS)
    - vlastní překladač pro nějaký jednoduchý jazyk
- databáze
    - zkusit si implementovat key-value store (jako Redis) s indexem přes klíče pomocí B-stromu nebo hashování
    - vlastní malá databáze, která si hlídá konzistenci cizích klíčů
    - in-memory databáze pro snadné testování aplikace
- matematika
    - symbolická úprava matematických výrazů (symbolická kalkulačka)
    - SAT
    - lineární optimalizace (simplexová metoda)
    - počítání s maticemi
    - numerická matematika
        - kořeny polynomů
        - integrace diferenciálních rovnic
        - dekompozice matic (LU rozklad)
        - fitování funkcí
- fyzika
    - simulace el. obvodů
    - simulace proudění kapalin, plynů
    - simulace sluneční soustavy (newtonovská gravitace)
    - rigid-body physics 2D, 3D
- grafika
    - konvoluční filtry
    - napsání vlastní 3D grafické pipeline nad CPU (vertex shader, fragment shader)
    - ray-tracing
    - automatický kontrast a jas obrázku
    - podepisování obrázků (detekce černé kopie souboru)
    - vyhledávání obrázků podle barev
    - tesselace povrchu podle displacement mapy
    - syntetické generování textur (perlin noise -> dřevo / mramor / ...)
- problémy v reálném světě (nejde řešit pěkně, je třeba použít neuristiky)
    - jízdní řády
    - obchodní cestující
    - batoh
    - loupežníci
    - optimální rozvržení školního rozvrhu
- cloud
    - vlastní message broker (rabbitMQ, Apache Kafka)
    - vlastní orchestrace kontejnerů pro docker
    - vlastní nástroj pro deployment (nahrávání přes FTP / SSH, ...)
    - nástroj pro prohlížení databáze (jako phpmyadmin, ale appka)
    - nástroj pro testování REST api, GraphQL api
    - služba pro ukládání souborů (object storage - amazon S3 apod.)
