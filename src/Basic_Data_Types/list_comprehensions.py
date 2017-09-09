# list_comprehensions.py
"""
https://hackerrank.com/challenges/list-comprehensions

You're given three integers, (x, y, z) representing the dimensions of a cuboid
along with an integer n. You have to print a list of all possible coordinates
given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n.

Here, 0 <= i <= x; 0 <= j <= Y; 0 <= k <= z.

Input Format:
    Four integers x, y, z, and n, each on four separate lines.

Constraints:
    Print the list in lexicographic increasing order.
"""


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Note: only using list comprehension here because that's the point of the
    # exercise. In reality, I'd use for loops.
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)
          if ((i + j + k) != n)])


if __name__ == '__main__':
    main()
