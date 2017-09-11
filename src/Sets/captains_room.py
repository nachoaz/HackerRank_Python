# captains_room.py
"""
https://www.hackerrank.com/challenges/py-the-captains-room
"""


from collections import Counter

def pythonic_main():
    k = int(input())
    counts = Counter(list(map(int, input().split())))
    print(counts.most_common()[-1][0])


def main():
    k = int(input())
    room_nums = list(map(int, input().split()))
    unique_rooms = set(room_nums)
    print( (K*sum(unique_rooms) - 1*sum(room_nums)) / (K - 1))


if __name__ == '__main__':
    main()
