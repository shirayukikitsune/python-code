pi = 3.14159


def run():
    r = float(input())

    volume = pi * r * r * r * 4.0 / 3.0

    print("VOLUME = %.3f" % volume)


if __name__ == '__main__':
    run()
