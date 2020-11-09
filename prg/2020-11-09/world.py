class World:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.__walls = []
        for _ in range(self.__width):
            col = []
            for _ in range(self.__height):
                col.append(False)
            self.__walls.append(col)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def set_wall(self, x, y, is_present):
        self.__walls[x][y] = is_present

    def create_border(self):
        for x in range(self.__width):
            self.set_wall(x, 0, True)
            self.set_wall(x, self.height - 1, True)
        for y in range(self.__height):
            self.set_wall(0, y, True)
            self.set_wall(self.width - 1, y, True)

    def draw(self, frame):
        for x in range(self.__width):
            for y in range(self.__height):
                frame.set_pixel(
                    x,
                    y,
                    "##" if self.__walls[x][y] else ". "
                )
