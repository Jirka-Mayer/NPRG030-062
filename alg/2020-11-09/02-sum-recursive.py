"""
Budeme implementovat sčítání pole na několik způsobů
"""


def sum_procedural(data):
    return 0


def sum_recursive_lin(data):
    return 0


def sum_recursive_log(data):
    return 0


def main():
    data = [5, 8, 6, 4, 3, 6, 8, 5, 4, 2]
    s = sum(data)
    sp = sum_procedural(data)
    sr_lin = sum_recursive_lin(data)
    sr_log = sum_recursive_log(data)

    print(s, sp, sr_lin, sr_log)


main()
