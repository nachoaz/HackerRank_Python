# no_idea.py
"""
https://www.hackerrank.com/challenges/no-idea
"""


def main():
    _, _ = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    a_set = set(map(int, input().split()))
    b_set = set(map(int, input().split()))

    happiness = 0

    for el in arr:
        if el in a_set:
            happiness += 1
        elif el in b_set:
            happiness += -1
    
    print(happiness)


if __name__ == '__main__':
    main()
