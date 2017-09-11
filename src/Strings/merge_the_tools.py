# merge_the_tools.py
"""
https://www.hackerrank.com/challenges/merge-the-tools
"""


def main():
    s = input()
    k = int(input())

    us = list()
    for ix_base in range(len(s) // k):
        t = s[ix_base*k:ix_base*k + k]
        u = ''
        already_seen_letters = set()
        for i in range(len(t)):
            if t[i] not in already_seen_letters:
                already_seen_letters.add(t[i])
                u += t[i]
        print(u)


if __name__ == '__main__':
    main()
