def run():
    a, b, c = map(float, input().split())

    pi = 3.14159

    triangulo = a * c / 2.0
    circulo = c * c * pi
    trapezio = (a + b) * c / 2.0
    quadrado = b * b
    retangulo = a * b

    print('TRIANGULO: %.3f' % triangulo)
    print('CIRCULO: %.3f' % circulo)
    print('TRAPEZIO: %.3f' % trapezio)
    print('QUADRADO: %.3f' % quadrado)
    print('RETANGULO: %.3f' % retangulo)


if __name__ == '__main__':
    run()
