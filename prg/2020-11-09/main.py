from frame import Frame
from world import World
from player import Player


def main():
    # vytvoř svět s hráčem a krabicemi
    world = World(20, 5)
    world.create_border()
    player = Player(6, 3, world)

    while True:
        # vykresli současný stav hry
        frame = Frame(world.width, world.height)
        world.draw(frame)
        player.draw(frame)
        frame.draw()

        # načíst input - co chce hráč dělat
        print()
        given_input = input("wasd> ")
        
        if given_input == "exit":
            break

        # aktualizovat stav hry
        if given_input == "w": player.move_up()
        if given_input == "a": player.move_left()
        if given_input == "s": player.move_down()
        if given_input == "d": player.move_right()


main()
