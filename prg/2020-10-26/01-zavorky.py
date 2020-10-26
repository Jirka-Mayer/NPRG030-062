"""
Použijte implementaci zásobníku z minulé úlohy a implementujte program,
který dokáže rozpoznat validní řetězec závorek.

Validní: "<>[{}()]()"
Nevalidní: "(({}" nebo "{}([]))" nebo "[[(){)]]"
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


def is_openning_brace(c):
    return c in ["(", "[", "{", "<"]


def corresponding_openning_brace(c):
    if c == ")": return "("
    if c == "]": return "["
    if c == "}": return "{"
    if c == ">": return "<"
    exit("Invalid function argument: " + str(c))


def is_valid(text):
    stack = Stack()
    for c in text:
        if is_openning_brace(c):
            stack.push(c)
        else:
            if stack.is_empty():
                print("Closing a not-openned brace")
                return False
            if stack.peek() != corresponding_openning_brace(c):
                print("Brace mismatch")
                return False
            stack.pop()
    
    if not stack.is_empty():
        print("Some braces weren't closed")
        return False
    
    return True


def main():
    print(is_valid("<>[{}()]()"))
    print(is_valid("(({}"))
    print(is_valid("{}([]))"))
    print(is_valid("[[(){)]]"))


main()
