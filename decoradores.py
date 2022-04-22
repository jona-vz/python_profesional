def decorador(func):
    def envoltura():
        func()
        print('Esto se añade a la funcion original')
    return envoltura


def saludo():
    print('Hola!')


def run():
    
    saludo()

    #ahora la decoramos
    saludo2 = decorador(saludo)
    saludo2()

if __name__ == '__main__':
    run()