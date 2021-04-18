MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def run():
    month = int(input())

    print(MONTHS[month - 1])


if __name__ == '__main__':
    run()
