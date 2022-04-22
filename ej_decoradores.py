def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura


@mayusculas
def mensaje (nombre):
    return f'{nombre}, recibiste un mensaje'


def run():
    print(mensaje('Cesar'))


if __name__ == '__main__':
    run()