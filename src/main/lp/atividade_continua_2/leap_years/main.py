def run():
    inicio = int(input())
    fim = int(input())

    contador = 0

    for ano in range(inicio, fim + 1):
        if ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0:
            contador = contador + 1
            print(ano)

    print("bissextos: %d" % contador)


if __name__ == '__main__':
    run()
