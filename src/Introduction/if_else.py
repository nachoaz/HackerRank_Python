# if_else.py
"""
https://www.hackerrank.com/challenges/py-if-else

Given an integer, n, peform the following conditional actions:
    * if n is odd, print Weird
    * if n is even and in the inclusive range of 2 to 5, print Not Weird
    * if n is even and in the inclusive range of 6 to 20, print Weird
    * if n is even and greater than 20, print Not Weird

Input Format:
    A single line containing a positive integer, n.

Constraints:
    1 <= n <= 100

Output Format:
    Print Weird if the number is weird, otherwise, print Not Weird
"""


def is_odd(num):
    return (num % 2) == 1


def main():
    n = int(input('\nPlease provide a positive integer:\n'))

    if is_odd(n):
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")


if __name__ == '__main__':
    main()
