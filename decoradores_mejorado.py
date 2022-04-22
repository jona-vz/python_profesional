def decorador(func):
    def envoltura():
        print('Esto se añade a la funcion original')
        func()
    return envoltura


def saludo():
    print('Hola!')
saludo = decorador(saludo)


def run():
    saludo()


if __name__ == '__main__':
    run()