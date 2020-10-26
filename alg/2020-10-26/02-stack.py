"""
Implementuj třídu Stack, která bude reprezentovat zásobník.
Chceme na něm operace:
- print (__repr__)
- push, pop
- seek
"""

class Stack():
    def __init__(self):
        self.__items = []

    def __repr__(self):
        return ", ".join([repr(item) for item in self.__items]) + " <--"

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        ret = self.__items[-1]
        del self.__items[-1]
        return ret

    def peek(self):
        return self.__items[-1]

    def is_empty(self):
        return len(self.__items) == 0

# =================

stack = Stack()

stack.push(5)
stack.push(10)
stack.push("ahoj")

print(stack)

print(stack.peek()) # ahoj

print(stack.pop()) # ahoj
print(stack.pop()) # 10
print(stack.pop()) # 5

if stack.is_empty():
    print("Je prázdný")
