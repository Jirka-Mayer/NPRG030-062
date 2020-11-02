from heap import Heap

h = Heap()

data = [5, 3, 8, 4, 3, 6, 9, 5]
for i in data:
    h.add(i)

while h.is_empty():
    print(h.pop())
