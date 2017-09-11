# designer_door_mat.py
"""
https://www.hackerrank.com/challenges/designer-door-mat
"""


def get_even_nums_up_to_num(num):
    'returns even numbers up to num; assumes num is even'
    return list(range(1, num + 2, 2))


def print_line_with_k_patterns(k, m):
    pattern = '.|.'
    print((pattern*k).center(m, '-'))


def print_top_part(n, m, even_nums):
    for i in even_nums:
        print_line_with_k_patterns(i, m)


def print_middle_part(m):
    print('WELCOME'.center(m, '-'))


def print_bottom_part(n, m, even_nums):
    for i in reversed(even_nums):
        print_line_with_k_patterns(i, m)


def main():
    n, m = map(int, input().split())
    even_nums = get_even_nums_up_to_num(n-2)

    print_top_part(n, m, even_nums)
    print_middle_part(m)
    print_bottom_part(n, m, even_nums)


if __name__ == '__main__':
    main()
