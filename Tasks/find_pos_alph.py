from string import ascii_lowercase


def position(alphabet):
    return "Position of alphabet: " + str(ascii_lowercase.index(alphabet.lower()) + 1)


if __name__ == '__main__':
    print(position(input()))
