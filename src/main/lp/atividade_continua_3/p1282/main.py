def read_channel_line():
    channel_name, subscriber_count, income, has_premium_content = input().split(sep=';')

    return {
               "channel_name": channel_name,
               "subscriber_count": int(subscriber_count),
               "income": float(income),
               "has_premium_content": has_premium_content == 'sim'
    }


def read_channels():
    channel_count = int(input())

    channels = []
    for i in range(channel_count):
        channels.append(read_channel_line())

    return channels


def read_extra_payments():
    premium_content = float(input())
    no_premium = float(input())

    return premium_content, no_premium


def calculate_channel_earnings(channel, extra):
    per_k_subs_amount = extra[0] if channel["has_premium_content"] else extra[1]
    per_k_subs_amount *= channel["subscriber_count"] // 1000

    return channel["income"] + per_k_subs_amount


def print_header():
    print('-----')
    print('BÔNUS')
    print('-----')


def print_channel_earnings(channel, extra):
    earnings = calculate_channel_earnings(channel, extra)
    print(f'{channel["channel_name"]}: R$ {earnings:.2f}')


def run():
    channels = read_channels()
    extra = read_extra_payments()

    print_header()
    for channel in channels:
        print_channel_earnings(channel, extra)


if __name__ == '__main__':
    run()
