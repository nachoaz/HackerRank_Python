# symmetric_difference_operation.py
"""
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation
"""


def main():
    _ = int(input())
    nset = set(map(int, input().split()))
    _ = int(input())
    bset = set(map(int, input().split()))

    print(len(nset.symmetric_difference(bset))) 


if __name__ == '__main__':
    main()
