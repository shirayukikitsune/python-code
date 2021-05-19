def run():
    id1, n1, p1 = map(float, input().split())
    id2, n2, p2 = map(float, input().split())

    total = n1 * p1 + n2 * p2

    print('VALOR A PAGAR: R$ %.2f' % total)


if __name__ == '__main__':
    run()
