def run():
    x = int(input())
    y = int(input())

    if x > y:
        x, y = y, x

    start = x + 2 if x % 2 == 1 else x + 1
    end = y

    total = 0
    for i in range(start, end, 2):
        total = total + i
    print(total)


if __name__ == '__main__':
    run()
