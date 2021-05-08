def run():
    ages_sum = 0
    count = 0

    while True:
        age = int(input())
        if age < 0:
            break

        ages_sum = ages_sum + age
        count = count + 1

    avg = ages_sum / count
    print(f'{avg:.2f}')


if __name__ == '__main__':
    run()
