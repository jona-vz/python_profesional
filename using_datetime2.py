from datetime import datetime

def run():
    my_datetime = datetime.now()
    print(my_datetime)

    my_str = my_datetime.strftime('%d/%m/%Y')
    print(f'Formato LATAM: {my_str}')
    my_str = my_datetime.strftime('%m/%d/%Y')
    print(f'Formato USA: {my_str}')
    my_str = my_datetime.strftime('Primero el año %Y luego el mes %m y por ultimo el dia %d')
    print(f'Formato personalizado: {my_str}')
    


if __name__ == '__main__':
    run()