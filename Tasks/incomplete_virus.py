def incomplete_virus(s):
    length = len(s)
    count = 0
    prefire = False
    for ddigit, digit in enumerate(s):
        if int(digit) >= 1 or prefire:
            count += 2 ** (length - ddigit - 1)
        if int(digit) > 1:
            prefire = True
    return count


if __name__ == '__main__':
    user_input = input()
    print(incomplete_virus(user_input))