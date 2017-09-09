# print_function.py
"""
https://www.hackerrank.com/challenges/python-print

Read an integer, N.

Without using any string methods, try to print the following:
    123...N
    (where ... represents the values in between).

Input Format:
    The first line contains an integer N.

Output Format:
    Output the answer as explained in the task.
"""


def main():
    N = int(input('Please enter an integer:\n'))
    print(*range(1, N+1), sep='')


if __name__ == '__main__':
    main()
