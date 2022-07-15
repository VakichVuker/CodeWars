def valid_parentheses(string):
    counter = 0
    for char in string:
        if char == '(':
            counter += 1
        if char == ')':
            counter -= 1
        if counter < 0:
            return False
    return True if counter == 0 else False


if __name__ == '__main__':
    print(valid_parentheses(input()))
