def run():
    my_set1 = {3, 4, 5}
    my_set2 = {5, 6, 7}

    #union
    my_set3 = my_set1 | my_set2
    print(my_set3)
    
    #interseccion
    my_set3 = my_set1 & my_set2
    print(my_set3)
    
    #diferencia
    my_set3 = my_set1 - my_set2
    print(my_set3)

    #diferencia simétrica
    my_set3 = my_set1 ^ my_set2
    print(my_set3)


if __name__ == '__main__':
    run()