# symmetric_difference.py
"""
https://www.hackerrank.com/challenges/symmetric-difference
"""


def main():
    m = int(input())
    mset = set(map(int, input().split()))

    n = int(input())
    nset = set(map(int, input().split()))

    for num in mset.symmetric_difference(nset):
        print(num)


if __name__ == '__main__':
    main()
