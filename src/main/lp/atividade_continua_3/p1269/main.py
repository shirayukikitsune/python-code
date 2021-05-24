def create_cart() -> list:
    items = list(map(int, input().split()))
    cart = []
    for item in items:
        add_item_to_cart(cart, item)
    return cart


def print_cart_items(cart: list) -> bool:
    if len(cart) > 0:
        print(*cart)
    return True


def add_item_to_cart(cart: list, item: int) -> bool:
    # Ordered insert
    i = 0
    while i < len(cart):
        if cart[i] > item:
            break
        i += 1
    cart[i:i] = [item]
    return True


def remove_item_from_cart(cart: list, item: int) -> bool:
    i = 0
    deleted = False
    while i < len(cart):
        if cart[i] == item:
            cart.pop(i)
            deleted = True
            break
        if cart[i] > item:
            break
        i += 1
    if not deleted:
        print(f'código {item} não encontrado')
    return True


def print_and_exit(cart: list) -> bool:
    print_cart_items(cart)
    return False


operations = {
    "exibir": print_cart_items,
    "adicionar": add_item_to_cart,
    "remover": remove_item_from_cart,
    "encerrar": print_and_exit,
}


def run():
    cart = create_cart()
    should_continue = True

    while should_continue:
        line = input().split()
        operation = line[0]
        args = [cart]
        if len(line) > 1:
            args.append(int(line[1]))
        should_continue = operations.get(operation, lambda x: False)(*args)


if __name__ == '__main__':
    run()
