# difference_operation.py
"""
https://www.hackerrank.com/challenges/py-set-difference-operation
"""


def main():
    _ = input()
    e_set = set(map(int, input().split()))
    _ = input()
    f_set = set(map(int, input().split()))

    print(len(e_set.difference(f_set)))


if __name__ == '__main__':
    main()
