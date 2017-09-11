# string_validators.py
"""
https://www.hackerrank.com/challenges/string-validators
"""


def main():
    s = input()
    
    if any([char.isalnum() for char in s]):
        print("True")
    else:
        print("False")

    if any([char.isalpha() for char in s]):
        print("True")
    else:
        print("False")

    if any([char.isdigit() for char in s]):
        print("True")
    else:
        print("False")

    if any([char.islower() for char in s]):
        print("True")
    else:
        print("False")

    if any([char.isupper() for char in s]):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
