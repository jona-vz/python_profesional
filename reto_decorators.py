def copyright_message(name, year):
    def copy(func):
        def wrapper(*args, **kwargs):
            res = str(func(*args, **kwargs)) + f'\nCopyright @ [{name}, {year}]. Any illegal reproduction of this content will result in immediate legal action.\n\n'
            return res
        return wrapper
    return copy


@copyright_message(name= 'Jonathan',year= 2022)
def isPalindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


@copyright_message(name= 'Jona',year= 2022)
def suma(a: int, b: int) -> int:
    return a + b


def run():
    print(isPalindrome("Ana"))
    print()
    print(suma(5,5))


if __name__ == '__main__':
    run()

'''
def copyright_message(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Copyright @ [Jonathan, 2022]. Any illegal reproduction of this following content will result in immediate legal action.\n\n')
        return result
    return wrapper
    

@copyright_message
def isPalindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    # if string == string[::-1]:
    #     print("Es un palindromo")
    # else:
    #     print("NO es un palindromo")
    return string == string[::-1]



def run():
    # isPalindrome("Anaa")
    print(isPalindrome("Ana"))

if __name__ == '__main__':
    run()
'''