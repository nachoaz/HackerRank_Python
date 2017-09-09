# loops.py
"""
https://www.hackerrank.com/challenges/python-loops

Read an integer N. For all non-negative integers i < N, print i squared.

Input Format:
    The first and only line contains the integer, N.

Constraints:
    1 <= N <= 20

Output Format:
    Print N lines, one corresponding to each i.
"""


def main():
    N = int(input("Please provide an integer:\n"))

    for i in range(N):
        print(i**2)


if __name__ == '__main__':
    main()
