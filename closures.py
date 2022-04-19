def word_multiplier (times: int):
    def multiplier (word: str):
        assert type(word) == str, "Solo puedes utilizar cadenas"
        return word * times
    return multiplier


def run():
    repeat_5 = word_multiplier(5)
    print(repeat_5("HELLO "))
    repeat_10 = word_multiplier(10)
    print(repeat_10("JONA "))


if __name__ == '__main__':
    run()