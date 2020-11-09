"""
Implementujte algoritmus merge sort.

(nemusí být na místě, chci radši přehlednost, než maximální efektivitu)
"""

def merge_sort(data):
    if len(data) == 1:
        return data
    
    middle = len(data) // 2
    left = merge_sort(data[0:middle])
    right = merge_sort(data[middle:])

    out = []

    while True:
        if len(left) == 0:
            out += right
            break
        if len(right) == 0:
            out += left
            break
        
        if left[0] < right[0]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))

    return out

def main():
    data = [5, 8, 6, 4, 3, 6, 8, 5, 4, 2]
    sorted_data = merge_sort(data)
    print(sorted_data)
    print(list(sorted(data)))
    assert sorted_data == list(sorted(data))

main()
