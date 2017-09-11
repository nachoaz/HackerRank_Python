# mutations.py
"""
https://www.hackerrank.com/challenges/python-mutations
"""


def main():
    s = input()

    # using comp instead of map cause "more pythonistas consider them clearer"
    i, c = [int(el) if el.isdigit() else elfor el in input().split()]
    
    print(s[:i] + c + s[i+1:])


if __name__ == '__main__':
    main()
