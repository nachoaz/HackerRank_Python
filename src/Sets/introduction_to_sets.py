# introduction_to_sets.py
"""
https://www.hackerrank.com/challenges/py-introduction-to-sets
"""


def main():
    n = int(input())
    heights = set(map(int, input().split()))

    print(sum(heights) / len(heights))


if __name__ == '__main__':
    main()
