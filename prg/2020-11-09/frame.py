class Frame:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.__pixels = []
        for _ in range(self.__width):
            col = []
            for _ in range(self.__height):
                col.append("..")
            self.__pixels.append(col)

    def set_pixel(self, x, y, value):
        # TODO: kontroluj okraje snímku + velikost pixelu
        self.__pixels[x][y] = value

    def draw(self):
        print("\n" * 10)
        for y in range(self.__height):
            for x in range(self.__width):
                print(self.__pixels[x][y], end="")
            print()
