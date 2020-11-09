"""
Budeme implementovat sčítání pole na několik způsobů
"""


def sum_procedural(data):
    acc = 0
    for x in data:
        acc += x
    return acc


def sum_recursive_lin(data):
    if len(data) == 1:
        return data[0]
    return data[0] + sum_recursive_lin(data[1:])


def sum_recursive_log(data):
    if len(data) == 1:
        return data[0]
    middle = len(data) // 2
    return sum_recursive_log(data[0:middle]) + sum_recursive_log(data[middle:])


def main():
    data = [5, 8, 6, 4, 3, 6, 8, 5, 4, 2] * 1000
    s = sum(data)
    sp = sum_procedural(data)
    sr_lin = sum_recursive_lin(data)
    sr_log = sum_recursive_log(data)

    print(s, sp, sr_lin, sr_log)


main()
