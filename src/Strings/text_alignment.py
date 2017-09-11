# text_alignment.py
"""
https://www.hackerrank.com/challenges/text-alignment
"""


def get_first_k_even_nums(k):
    return [i for i in range(1, 2*k) if i%2 == 1]


def get_even_nums_and_width(thickness):
    even_nums = get_first_k_even_nums(thickness)
    tri_extra = even_nums.index(thickness)
    width = tri_extra + thickness + 3*thickness + thickness + tri_extra
    return even_nums, width


def draw_lupper_triangle(c, even_nums, width):
    for i in even_nums:
        triangle_part = (c * i).center(even_nums[-1])
        print(triangle_part.ljust(width))


def draw_h_pillars(c, thickness, width):
    for _ in range(thickness + 1):
        print((c*thickness + ' '*3*thickness + c*thickness).center(width))


def draw_h(c, thickness, width):
    draw_h_pillars(c, thickness, width)
    for _ in range((thickness+1)//2):
        print((c*thickness*5).center(width))
    draw_h_pillars(c, thickness, width)


def draw_rlower_triangle(c, even_nums, width):
    for i in reversed(even_nums):
        triangle_part = (c * i).center(even_nums[-1])
        print(triangle_part.rjust(width))


def generate_hackerrank_logo(c, thickness):
    even_nums, width = get_even_nums_and_width(thickness)
    
    draw_lupper_triangle(c, even_nums, width)
    draw_h(c, thickness, width)
    draw_rlower_triangle(c, even_nums, width)


def main():
    c = 'H'
    thickness = int(input())
    generate_hackerrank_logo(c, thickness)


if __name__ == '__main__':
    main()
