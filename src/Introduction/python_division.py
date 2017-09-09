# python_division.py
"""
https://www.hackerrank.com/challenges/python-division

Read two integers and print two lines. The first line should contain integer
division (a // b), and the second should contain float division (a / b).

Input Format:
    The first line contains the first integer, a. The second line contains the
    second integer, b.

Output Format:
    Print the two lines as described above.
"""


def main():
    a = int(input('Please enter the dividend.\n'))
    b = int(input('Please enter the divisor.\n'))

    print(a // b)
    print(a / b)

if __name__ == '__main__':
    main()
