def run():
    seller = input()
    salary = float(input())
    sales = float(input())

    total = salary + sales * 0.15

    print('TOTAL = R$ %.2f' % total)


if __name__ == '__main__':
    run()
