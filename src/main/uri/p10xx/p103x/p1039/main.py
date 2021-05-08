import sys
from math import sqrt


def run():
    for line in sys.stdin:
        r1, x1, y1, r2, x2, y2 = map(int, line.split())

        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        text = 'RICO'
        if r1 < distance + r2:
            text = 'MORTO'
        print(text)


if __name__ == '__main__':
    run()
