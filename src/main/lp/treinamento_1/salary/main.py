def run():
    number = int(input())
    hours = int(input())
    salary_per_hour = float(input())

    salary = hours * salary_per_hour

    print('NUMBER = %d' % number)
    print('SALARY = U$ %.2f' % salary)


if __name__ == '__main__':
    run()
