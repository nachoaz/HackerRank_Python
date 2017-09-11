# text_wrap.py
"""
https://www.hackerrank.com/challenges/text-wrap
"""


import textwrap


def main():
    s = input()
    w = int(input())

    print(textwrap.fill(s, w))


if __name__ == '__main__':
    main()
