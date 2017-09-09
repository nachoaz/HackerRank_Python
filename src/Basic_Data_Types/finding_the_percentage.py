# finding_the_percentage.py
"""
https://www.hackerrank.com/challenges/finding-the-percentage

You have a record of n students. Each record contains the student's name and
their percent marks in Maths, Physics, and Chemistry. The marks can be floating
values. The user enters some integer (n) followed by the names and marks for n
students. You are required to save the record in a dictionary data type. The
user then enters a students name. Output the average percentage marks obtained
by that student, correct to two decimal places.

Input Format:
    The first line contains the integer, n. The next n lines contains the name
    and makrs obtained by that student separated by a space. The final line
    contains the name of a particular student previously listed.

Constraints:
    2 <= n <= 10
    0 <= marks <= 100

Output:
    Print one

"""


def get_mean(grades):
    'receives grades as nonempty list, returns mean as float'
    return sum(grades) / len(grades)


def main():
    n = int(input())

    gradebook = dict()
    for _ in range(n):
        name, *grades_as_strs = input().split()
        grades = list(map(float, grades_as_strs))
        gradebook[name] = grades

    queried_name = input()
    print("{0:.2f}".format(get_mean(gradebook[queried_name])))

if __name__ == '__main__':
    main()
