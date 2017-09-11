# string_formatting.py
"""
https://www.hackerrank.com/challenges/python-string-formatting
"""


def main():
    n = int(input())
    spac = len('{:b}'.format(n))
    
    for i in range(1, n+1):
        print('{:d}'.format(i).rjust(spac), \
              '{:o}'.format(i).rjust(spac), \
              '{:X}'.format(i).rjust(spac), \
              '{:b}'.format(i).rjust(spac))


if __name__ == '__main__':
    main()
