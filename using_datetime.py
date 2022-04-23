import datetime


def run():
    my_time = datetime.datetime.now()
    print(my_time)

    my_day = datetime.date.today()
    print(my_day)
    print()
    print(f'Year: {my_day.year}')
    print(f'Month: {my_day.month}')
    print(f'Day: {my_day.day}')


if __name__ == '__main__':
    run()
