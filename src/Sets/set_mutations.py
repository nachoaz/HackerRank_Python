# set_mutations.py
"""
https://www.hackerrank.com/challenges/py-set-mutations
"""


def main():
    _ = input()
    a_set = set(map(int, input().split()))
    n = int(input())

    for _ in range(n):
        cmd, _ = input().split()
        eval('a_set.{}(set({}))'.format(cmd, list(map(int, input().split()))))

    print(sum(a_set))


if __name__ == '__main__':
    main()
