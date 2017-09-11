# capitalize.py
"""
https://www.hackerrank.com/challenges/capitalize
"""


def main():
    s = input()
    print(' '.join([word.capitalize() for word in s.split(' ')]))


if __name__ == '__main__':
    main()
