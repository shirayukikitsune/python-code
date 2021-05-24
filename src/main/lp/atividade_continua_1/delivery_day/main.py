dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']


def run():
    dia = input()
    prazo = int(input())

    if prazo == 0:
        print('chega hoje!')
    else:
        dia_entrega = (dias.index(dia) + prazo) % len(dias)
        print('sera entregue %s' % dias[dia_entrega])


if __name__ == '__main__':
    run()
