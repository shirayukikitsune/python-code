def show_table(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')


def show_table_for_range(a, b):
    if a > b:
        print('Nenhuma tabuada no intervalo!')
        return
    for n in range(a, b + 1):
        show_table(n)
        print('-' * 10)


def run():
    a = int(input())
    b = int(input())

    show_table_for_range(a, b)


if __name__ == '__main__':
    run()
