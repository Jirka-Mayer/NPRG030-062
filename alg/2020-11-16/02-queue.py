"""
Implementujte frontu pomocí spojového seznamu.
"""

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Queue:
    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, item):
        node = Node(item, self.__first)
        self.__first = node

        if self.__last is None:
            self.__last = self.__first

    def dequeue(self):
        node = self.__first
        node_before_that = None

        if node is None:
            return None

        while node.next is not None:
            node_before_that = node
            node = node.next

        if node_before_that is None:
            self.__first = None
            self.__last = None
        else:
            node_before_that.next = None
            self.__last = node_before_that
        
        return node.item


def main():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())


main()
