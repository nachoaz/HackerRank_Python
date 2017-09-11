# discard_remove_pop
"""
https://www.hackerrank.com/challenges/py-set-discard-remove-pop
"""


def main():
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        cmd, *arg = input().split()
        if cmd == 'pop':
            s.pop()
        else:
            eval('s.{}({})'.format(cmd, arg[0]))

    print(sum(s))


if __name__ == '__main__':
    main()
