"""
Implementujte datovou strukturu "trije" (anglicky třída Trie) jako kontejner,
který si bude pamatovat množinu slov (lower-case, pismena).

Bude mít metody .add(w) pro přidávání slova a .enumerate() pro vypsání
slov do seznamu a ten vrátí.

Potom ji použijte k setřízení několika testovacích slov.
"""

slova = [
    "lorem", "ipsum", "dolor", "sit", "amet",
    "a", "aa", "ab", "b",
    "ahoj", "ne", "nejneobhospodarovavatelnejsimi"
]


class Node:
    def __init__(self):
        self.children = [None] * (ord("z") - ord("a") + 1)
        self.filled = False

    def ch_to_i(self, ch):
        return ord(ch) - ord("a")

    def i_to_ch(self, i):
        return chr(ord("a") + i)

    def add(self, w):
        if w == "":
            self.filled = True
            return

        i = self.ch_to_i(w[0])

        if self.children[i] is None:
            self.children[i] = Node()

        self.children[i].add(w[1:])

    def enumerate(self):
        if self.filled:
            yield ""
        
        for i, child in enumerate(self.children):
            if child is None:
                continue

            for w in child.enumerate():
                yield self.i_to_ch(i) + w


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, w):
        self.root.add(w)

    def enumerate(self):
        return self.root.enumerate()


def main():
    t = Trie()
    for s in slova:
        t.add(s)

    for s in t.enumerate():
        print(s)


main()
