import sys


def run():
    jewels = set()

    for jewel in sys.stdin:
        jewels.add(jewel)

    print(len(jewels))


if __name__ == '__main__':
    run()
