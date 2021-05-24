def run():
    timings = []
    while True:
        timing = int(input())
        if timing < 0:
            break

        timings.append(timing)

    avg = 0
    for t in timings:
        avg += t / len(timings)

    print(f'MEDIA: {avg:.2f}')

    for t in timings:
        if t < avg:
            print(t)


if __name__ == '__main__':
    run()
