def bake_cake():
    d, i, b = map(int, input().split())
    prices = list(map(int, input().split()))

    max_cakes = 0

    for j in range(b):
        data = list(map(int, input().split()))
        q = data.pop(0)
        price = 0
        for k in range(q):
            ingredient = data.pop(0)
            amount = data.pop(0)
            price = price + prices[ingredient] * amount
        cakes = d // price
        if cakes > max_cakes:
            max_cakes = cakes

    print(max_cakes)


def run():
    t = int(input())

    for i in range(t):
        bake_cake()


if __name__ == '__main__':
    run()
