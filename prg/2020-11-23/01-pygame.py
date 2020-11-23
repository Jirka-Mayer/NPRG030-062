"""
Ukázkový příklad použití pygame.
Hodně vysvětlování...
"""

# https://www.pygame.org/docs/tut/PygameIntro.html

import sys
import os
import pygame

# relativní cesta vzhledem k tomuto souboru -> absolutní cesta
def fix_path(p):
    return os.path.dirname(os.path.realpath(__file__)) + "/" + p

# připraví pygame (musí se zavolat)
# pozn. - VS Code - linter (.vscode/settings.json)
pygame.init()

# rozměry okna, do kterého budeme kreslit
width = 960
height = 720

# vytvoříme okno, do kterého budeme kreslit,
# dostaneme objekt typu Surface do kterého můžeme kreslit
screen = pygame.display.set_mode((width, height))

# vytvoříme hodiny, které hlídají kolik času uplynulo od posledního snímku
clock = pygame.time.Clock()

# --- INITIALIZE ---

# vektor rychlosti míčku (x, y), v "pixelech za snímek"
velocity = pygame.Vector2(3, 2)

# načteme obrázek míčku, opět dostaneme objekt typu Surface
ball = pygame.image.load(fix_path("intro_ball.png"))

# dostaneme obdélník (0, 0, w, h) kde w, h jsou rozměry obrázku
# objekt typu Rect, pozor, interně vždy celočíslené hodnoty, ačkoliv příjmá float
ballrect = ball.get_rect()

# nekonečná smyčka animace
while True:

    # --- UPDATE ---
    
    # přečteme události, které nastaly
    for event in pygame.event.get():
        # a zajistíme exit při požadavku na zavření okna
        if event.type == pygame.QUIT:
            sys.exit()

    # provedeme pohyb míčku
    ballrect = ballrect.move(velocity)

    # upravíme vektor rychlosti míčku, pokud "narazil" na stěnu
    if ballrect.left < 0 or ballrect.right > width:
        velocity.x = -velocity.x
    if ballrect.top < 0 or ballrect.bottom > height:
        velocity.y = -velocity.y

    # --- DRAW ---

    # vyčístíme obrazovku (nastavíme všude černou)
    screen.fill(pygame.Color(0, 0, 0))

    # vykreslíme míček na danou pozici
    screen.blit(ball, ballrect)
    
    # zapíšeme objekt "screen", "někam", aby se nám zobrazil v okně
    # (do těď jsme kreslili jen někam do paměti, teď to zobrazíme na obrazovku)
    pygame.display.flip()

    # budeme spát (nic nedělat) tak dlouho, aby jeden snímek trval 1/30 sekundy
    # to nám zajistí, že nebudeme mít 100% vytížení CPU, nebudeme kreslit "co nejvíc" snímků
    #clock.tick(30)
