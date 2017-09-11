# the_minion_game.py
"""
https://www.hackerrank.com/challenges/the-minion-game
"""


def main():
    s = input()
    n = len(s)

    stuarts_score = 0
    kevins_score = 0

    for i in range(n):
        if s[i] in {'A', 'E', 'I', 'O', 'U'}:
            kevins_score += (n - i)
        else:
            stuarts_score += (n - i)

    if stuarts_score > kevins_score:
        print("Stuart {}".format(stuarts_score))
    elif kevins_score > stuarts_score:
        print("Kevin {}".format(kevins_score))
    else:
        print("Draw")


if __name__ == '__main__':
    main()
