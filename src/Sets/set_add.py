# set_add.py
"""
https://www.hackerrank.com/challenges/py-set-add
"""


def main():
    n = int(input())

    countries = set()
    for _ in range(n):
        countries.add(input())

    print(len(countries))


if __name__ == '__main__':
    main()
