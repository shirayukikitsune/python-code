def run():
    n = int(input())

    for i in range(2, n + 1, 2):
        print("{:d}^2 = {:d}".format(i, i * i))


if __name__ == '__main__':
    run()
