def run():
    inicio = int(input())
    fim = int(input())

    primos = [2]

    for i in range(3, fim + 1, 2):
        eh_primo = True
        for n in primos:
            if i % n == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)

    c = 0
    for n in primos:
        if n >= inicio:
            print(n)
            c = c + 1
    print(f'primos: {c}')


if __name__ == '__main__':
    run()
