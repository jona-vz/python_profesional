def isPalindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def run():
    print(isPalindrome("ANA"))


if __name__ == '__main__':
    run()