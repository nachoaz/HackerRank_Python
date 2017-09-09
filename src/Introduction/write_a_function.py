# write_a_function.py
"""
https://www.hackerrank.com/challenges/write-a-function

Given the year, you have to write a function to check if the year is leap or
not.

Input Format:
    Read y, the year that needs to be checked.

Constraints:
    1900 <= y <= 1e5

Output Format:
    Output is taken care of by the template. Your function must return a boolean
    value (True/False).
"""


def is_leap_year(year):
    is_leap = False

    if year % 400 == 0:
        is_leap = True
    elif year % 100 == 0:
        is_leap = False
    elif year % 4 == 0:
        is_leap = True

    return is_leap


def main():
    y = int(input('Please enter a year:\n'))
    print(is_leap_year(y))


if __name__ == '__main__':
    main()
