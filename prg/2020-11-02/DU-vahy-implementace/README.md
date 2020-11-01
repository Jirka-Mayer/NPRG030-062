# Váhy - Implementace

**Backstory:** Máme N zlatých kuliček, jedna je vadná (je lehčí), chceme ji nalézt na co nejméně vážení. Máme rovnoramenné váhy, na miskách vah může být neomezený počet kuliček, váhy dokážou určit rovnost.

Napište program, který vadnou kuličku najde na co nejmenší počet vážení. K dispozici budete mít modul `assignment`, který vám poskytne seznam kuliček a rovnoramenné váhy. Modul si stáhněte [zde](https://recodex.mff.cuni.cz/api/v1/uploaded-files/97e954a4-1c61-11eb-8e81-005056ad4f31/download) a dejte si ho vedle svého souboru s řešením, abyste mohli program testovat u sebe. Pojmenujte ho `assignment.py`.

Modul definuje dvě funkce:

- `assignment.get_balls()` která vrátí seznam koulí. Koule jsou očíslované od `0` do `N - 1`.
- `assignment.weigh([1, 8, ...], [5, 7, ...])` funkce, která reprezentuje váhy. Dva argumenty reprezentují mistky vah. Funkce vrátí název **lehčí** misky (tedy `"left"`, nebo `"right"`), nebo `"same"`, pokud jsou misky stejně těžké.

Váš program má za úkol vypsat na standardní výstup číslo vadné koule (vždy právě jedna taková existuje).

Kdybychom měli pouze 3 koule, mohli bychom napsat následující program:

```py
import assignment

balls = assignment.get_balls()  # [0, 1, 2]

result = assignment.weigh(balls[0:1], balls[1:2])  # [0] >?< [1]

if result == "left":
    print(balls[0])  # 0
elif result == "right":
    print(balls[1])  # 1
else:
    print(balls[2])  # 2
```

Takže cílem je rozšířit tento kus kódu, aby dokázal pracovat s libovolným počtem koulí.

Pokud bude váš algoritmus používat moc vážení, váhy se rozbijí, což je simulováno vyhozením výjimky (program spadne).

Pro testování vašeho řešení můžete modifikovat první tři řádky v souboru `assignment.py`:

```py
ball_count = 3  # počet koulí
target_ball = 2  # číslo vadné koule
max_weigh_count = 1  # kolik vážení váhy snesou, než se rozbijí

# ... zbytek souboru ...
```

**Pro vtipálky:** Věřte, že obyčejné `print(assignment.target_ball)` vám recodex nevezme, protože soubor `assignment.py` je v recodexu implementován jinak. Ale můžete to použít ve vašem kódu během lazení.
