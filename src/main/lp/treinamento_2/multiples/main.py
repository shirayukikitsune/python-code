def run():
    a, b = map(int, input().split())

    multiplos = a % b == 0 or b % a == 0

    print(multiplos and 'Sao Multiplos' or 'Nao sao Multiplos')


if __name__ == '__main__':
    run()
