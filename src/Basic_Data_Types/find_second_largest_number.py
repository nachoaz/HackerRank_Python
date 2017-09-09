# find_second_largest_number.py
"""
https://hackerrank.com/challenges/find-second-maximum-number-in-a-list

You are given n numbers. Store them in a list and find the second largest
number.

Input Format:
    The first line contains n. The second line contains an array A[] of n
    integers, each separated by a space.

Constraints:
    2 <= n <= 10
    -100 <= A[i] <= 100 for all i

Output Format:
    Print the value of the second largest number.

Here, we could use two solutions:
    (1) An O(nlogn) time solution consisting of turning the list into a set, 
        sorting it, and returning the second largest. Note: O(nlogn) because
        sorted() uses Timsort.
        print(sorted(set(A))[-2])
    (2) A O(n) time solution consisting of walking through the set, tracking
        the first and second largest:
            second_largest = float('-inf')
            largest = float('-inf')
            for i in range(n):
                if A[i] > largest:
                    second_largest = largest
                    largest = A[i]
                elif second_largest < A[i] < largest:
                    second_largest = A[i]

            print(second_largest)

Keeping in mind that because the list is of at most 10 numbers, the O(nlogn)
solution isn't too much worse than the O(n) solution and showing deference to
the principle of 'readability counts', I opted for the O(nlogn) solution.
"""


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    
    if len(set(A)) >= 2:
        print(sorted(set(A))[-2])
    else:
        print(list(set(A))[0])


if __name__ == '__main__':
    main()
