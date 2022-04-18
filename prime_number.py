from unittest import result


def isPrime(number: int) -> bool:
    result: list = [i for i in range(2, number) if number % i == 0]
    return len(result) == 0


def run():
    print(isPrime(11))


if __name__ == '__main__':
    run()