import sys


def has_repeated_digits(num):
    digits = [False] * 10
    while num > 0:
        digit = num % 10
        if digits[digit]:
            return True
        digits[digit] = True
        num = num // 10

    return False


def run():
    for line in sys.stdin:
        n, m = map(int, line.split())

        c = 0
        for i in range(n, m + 1):
            if not has_repeated_digits(i):
                c = c + 1
        print(c)


if __name__ == '__main__':
    run()
