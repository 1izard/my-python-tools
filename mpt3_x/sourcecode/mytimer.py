from datetime import datetime, timedelta
import math
from time import sleep


def parse_to_display_format(value):
    if value <= 0:
        return '00'
    return '0' * (1 - int(math.log10(float(value)))) + str(int(value))


def main():
    timer_sec = 0
    timer_min = 0
    timer_hour = 0

    d_now = datetime.now()
    td_1s = timedelta(seconds=1)
    d_next = d_now + td_1s

    while True:
        print('\r{}:{}:{}'.format(parse_to_display_format(timer_hour),
                                  parse_to_display_format(timer_min),
                                  parse_to_display_format(timer_sec)), end='')
        sleep((d_next - datetime.now()).total_seconds())
        timer_sec += 1
        if timer_sec >= 60:
            timer_min += 1
            timer_sec = 0
        if timer_min >= 60:
            timer_hour += 1
            timer_min = 0
        d_next += td_1s


if __name__ == '__main__':
    main()
