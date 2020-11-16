"""
Implementujte run-legth-encoding kompresi textového souboru
Soubor feep.pgm zpracujte řádek po řádku a vyrobte soubor feep.pgm.rle

Každý řádek vstupu je posloupnost slov, oddělených mezerou (slovo je zde číslo, ale nemusí to být číslo).
RLE kóduje posloupnost slov do dvojic <slovo, počet_opakování>.

Čili vstupní řádek:
0 0 0 0 1 1 aa aa foo foo foo foo

Bude RLE-zakódován následovně:
0 4 1 2 aa 2 foo 4
"""

import sys


def bite_tokens(tokens):
    token = tokens[0]

    count = -1
    for i in range(len(tokens)):
        if tokens[i] != token:
            count = i
            break

    if count == -1:
        count = len(tokens)

    return tokens[count:], token, count


def rle_encode_line(line):
    tokens = line.split()
    output_tokens = []
    
    while len(tokens) > 0:
        remaining_tokens, token, count = bite_tokens(tokens)
        tokens = remaining_tokens

        output_tokens.append(token)
        output_tokens.append(str(count))

    return " ".join(output_tokens)


def rle_encode(file_in, file_out):
    for line in file_in:
        file_out.write(rle_encode_line(line) + "\n")


def main():
    with open("feep.pgm", "r") as f:
        rle_encode(f, sys.stdout)

    
main()
