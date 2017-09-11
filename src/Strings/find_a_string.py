# find_a_string.py
"""
https://www.hackerrank.com/challenges/find-a-string
"""


def count_substr(my_str, my_substr):
    pstart_ixs = list()
    for i in range(len(my_str)):
        if my_str[i] == my_substr[0]:
            pstart_ixs.append(i)

    # remove ixs that could not possibly be a start_ix of substr
    pstart_ixs = [ix for ix in pstart_ixs if ix <= len(my_str) - len(my_substr)]

    count = 0
    for pstart_ix in pstart_ixs:
        if my_str[pstart_ix:pstart_ix+len(my_substr)] == my_substr:
            count += 1

    return count


def count_substr_pythonic(my_str, my_substr):
    count = start = 0

    while True:
        start = my_str.find(my_substr, start) + 1
        if start > 0:
            count += 1
        else:
            break

    return count


def main():
    my_str = input()
    my_substr = input()

    count = count_substr(my_str, my_substr)
    print(count)


if __name__ == '__main__':
    main()
