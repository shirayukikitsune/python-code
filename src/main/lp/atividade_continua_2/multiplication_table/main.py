def run():
    n = int(input())

    for i in range(1, 11):
        resultado = i * n
        print("{} x {} = {}".format(n, i, resultado))


if __name__ == '__main__':
    run()
