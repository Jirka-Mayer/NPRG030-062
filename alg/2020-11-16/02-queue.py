"""
Implementujte frontu pomocí spojového seznamu.
"""

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Queue:
    def __init__(self):
        pass

    def enqueue(self, item):
        pass

    def dequeue(self):
        return None


def main():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())


main()
