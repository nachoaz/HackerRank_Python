# arithmetic_operators.py
"""
https://www.hackerrank.com/challenges/python-arithmetic-operators

Read two integers from STDIN and print three lines where:
    (1) The first line contains the sum of the two numbers.
    (2) The second line contains the difference of the two numbers (first -
    second)
    (3) The third line contains the product of the two numbers

Input Format:
    The first line contains the first integer, a. The second line contains the
    second integer, b.

Constraints:
    1 <= a <= 1e10
    1 <= b <= 1e10

Output Format:
    Print the three lines as explained above.
"""

def main():
    a = int(input('Please provide a positive integer:\n'))
    b = int(input('Please provide a positive integer:\n'))

    print(a + b)
    print(a - b)
    print(a * b)

if __name__ == '__main__':
    main()
