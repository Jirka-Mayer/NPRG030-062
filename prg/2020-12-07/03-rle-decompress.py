"""
Implementujte program, který vezme soubor feep.pgm.rle a vrátí původní feep.pgm
"""

import os
import sys


def fix_path(p):
    return os.path.dirname(os.path.realpath(__file__)) + "/" + p


def decompress_line(line, index):
    tokens = line.strip().split()
    
    if len(tokens) % 2 != 0:
        raise Exception("Odd number of tokens on line: {}".format(index))

    output_tokens = []

    for i in range(len(tokens) // 2):
        token = tokens[i * 2]
        count = tokens[i * 2 + 1]

        try:
            count = int(count)
            assert count > 0
        except:
            raise Exception(
                "Token {} is not a valid count, on line {}."
                    .format(i * 2 + 1, index)
            )

        output_tokens += [token] * count

    return " ".join(output_tokens)


def decompress_file(file_in, file_out):
    for i, line in enumerate(file_in):
        file_out.write(decompress_line(line, i + 1) + "\n")


def main():
    with open(fix_path("feep.pgm.rle"), "r") as f:
        decompress_file(f, sys.stdout)


main()
