def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print('')


def troca(v, i, j):
    v[i],v[j] = v[j],v[i]


def empurra(v, n):
    for i in range(n - 1):
        if v[i] > v[i+1]:
            troca(v, i, i+1)


def bubble_sort(v, n):
    exibe(v, n)
    tam = n
    while tam > 1:
        empurra(v, tam)
        exibe(v, tam)
        tam = tam - 1
    exibe(v, n)


def run():
    bubble_sort([40, 20, 50, 30, 10], 5)


if __name__ == '__main__':
    run()
