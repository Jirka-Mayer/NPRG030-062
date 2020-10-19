# použití hornerova schématu pro převod "str" -> "int"

given_text = "2851"

acc = 0

lookup = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

for c in given_text:
    acc = acc * 10 + lookup[c]

print(type(acc))
print(acc)
