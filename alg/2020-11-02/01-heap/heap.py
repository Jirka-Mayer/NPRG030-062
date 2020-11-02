class Heap():
    def __init__(self):
        self.__items = []

    def __repr__(self):
        start = 0
        end = 0
        rep = ""
        
        while start < len(self.__items):
            if end < len(self.__items):
                end_rounded = end
            else:
                end_rounded = len(self.__items)

            rep += repr(self.__items[start:(end_rounded + 1)]) + "\n"
            start = self.__left(start)
            end = self.__right(end)

        return rep

    def is_empty(self):
        return len(self.__items) == 0

    def add(self, item):
        self.__items.append(item)

        i = len(self.__items) - 1
        while True:
            p_i = self.__parent(i)

            if i == 0:
                break

            if self.__items[p_i] <= self.__items[i]:
                break

            # strč uzel směrem ke kořeni
            tmp = self.__items[p_i]
            self.__items[p_i] = self.__items[i]
            self.__items[i] = tmp

            # jdi nahoru za bublajícím prvkem
            i = p_i

    def pop(self):
        # TODO: Na procvičení doma
        pass

    def __parent(self, i):
        return (i - 1) // 2

    def __left(self, i):
        return 2 * i + 1

    def __right(self, i):
        return 2 * i + 2
