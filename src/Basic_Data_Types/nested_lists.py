# nested_lists.py
"""
https://www.hackerrank.com/challenges/nested-list

Given the names and grades for each student in a Physics class of n students,
store them in a nested list and print the name(s) of any student(s) having the
second lowest grade.

Note: If there are multiple students with the same grade, order their names
alphabetically and print each name on a new line.

Input Format:
    The first line contains an integer (n), the number of students.
    The 2n subsequent lines describe each student over 2 lines; the first line
    contains a student's name, and the second line contains their grade.

Constraints:
    2 <= n <= 5
    There will always be one or more students having the second lowest grade.

Output Format:
    Print the name(s) of any student(s) having the second lowest grade in
    Physics; if there are multiple students, order their names alphabetically
    and print each one on a new line.

Even though the point of the exercise is to use a nested list, I'm gonna use a
defaultdict instead because the solution is much neater that way.
"""


from collections import defaultdict


def get_second_lowest_grade(grades):
    second_lowest = float('inf')
    lowest = float('inf')
    for grade in grades.keys():
        if grade < lowest:
            second_lowest = lowest
            lowest = grade
        elif lowest < grade < second_lowest:
            second_lowest = grade

    return second_lowest


def main():
    n = int(input())
    grades = defaultdict(list)

    for _ in range(n):
        name = input()
        grade = float(input())
        grades[grade].append(name)

    second_lowest = get_second_lowest_grade(grades)
    print('\n'.join(sorted(grades[second_lowest])))


if __name__ == '__main__':
    main()
