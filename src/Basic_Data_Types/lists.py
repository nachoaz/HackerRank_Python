# lists.py
"""
https://www.hackerrank.com/challenges/python-lists

Consider a list (list = []). You can perform the following commands:
    * insert i, e: Insert integer e at position i.
    * print: Print the list.
    * remove e: Delete the first occurrence of integer e.
    * sort: Sort the list.
    * pop: Pop the last element from the list.
    * reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed above. Iterate through each
command in order and perform the corresponding operation on your list.

Input Format:
    The first line contains an integer, n, denoting the number of commands. Each
    line i of the n subsequent lines contains one of the commands described
    above.

Constraints:
    The elements added to the list must be integers.

Output Format:
    For each command of type print, print the list on a new line.
"""


def main():
    N = int(input('How many commands will you enter?'))

    L = []

    for i in range(N):
        msg = 'Insert a command and its arguments, separated by a space'
        line = input(msg).split()
        if line[0] == "insert":
            L.insert(int(line[1]), int(line[2]))
        elif line[0] == "print":
            print(L)
        elif line[0] == "remove":
            L.remove(int(line[1]))
        elif line[0] == "append":
            L.append(int(line[1]))
        elif line[0] == "sort":
            L.sort()
        elif line[0] == "pop":
            L.pop()
        elif line[0] == "reverse":
            L.reverse()


if __name__ == "__main__":
    main()
