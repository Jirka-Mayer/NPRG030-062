from heap import Heap

h = Heap()

print("Vkládáme prvky:")

data = [5, 3, 8, 4, 3, 6, 9, 5]
for i in data:
    h.add(i)
    print(h)

# print("Vytahujeme prvky:")
# while not h.is_empty():
#     print(h.pop())
