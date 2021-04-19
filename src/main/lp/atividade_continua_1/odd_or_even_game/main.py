def run():
    x = int(input())

    odd = x - 1 - (0 if x % 2 == 0 else 1)
    even = x + 1 + (1 if x % 2 == 0 else 0)

    print('{:d} {:d}'.format(odd, even))


if __name__ == '__main__':
    run()
