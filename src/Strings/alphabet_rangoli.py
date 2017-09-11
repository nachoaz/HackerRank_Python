# alphabet_rangoli.py
"""
https://www.hackerrank.com/challenges/alphabet-rangoli
"""


import string


def main():
    alph = string.ascii_lowercase

    n = int(input())
    m = (n + (n-1)) + ((n + (n-1)) - 1)

    for i in list(range(1, n+1)) + list(range(n-1, 0, -1)):
        rside = list(alph[:n][-i:])
        lside = list(alph[:n][-i:][1:][::-1])
        print('-'.join((lside + rside)).center(m, '-'))


if __name__ == '__main__':
    main()
