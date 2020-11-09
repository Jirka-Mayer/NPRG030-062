class Player:
    def __init__(self, x, y, world):
        self.__x = x
        self.__y = y
        self.__world = world

    def move_up(self):
        if self.__y == 0:
            return
        self.__y -= 1

    def move_down(self):
        if self.__y == self.__world.height - 1:
            return
        self.__y += 1

    def move_left(self):
        if self.__x == 0:
            return
        self.__x -= 1

    def move_right(self):
        if self.__x == self.__world.width - 1:
            return
        self.__x += 1

    def draw(self, frame):
        frame.set_pixel(self.__x, self.__y, ":)")
