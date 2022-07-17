def is_one(n):  # if number is already a square
    return int(n ** (1 / 2)) == n ** (1 / 2)


def is_two(n):  # Fermat's theorem on sums of two squares
    i = 2
    while i * i <= n:
        k = 0
        if n % i == 0:
            while n % i == 0:
                k += 1
                n = n // i
            if i % 4 == 3 and k % 2 == 1:
                return False
        i += 1
    return n % 4 != 3


def is_three(n):  # Legendre's three-square theorem
    while n % 4 == 0:
        n /= 4
    return n % 8 != 7


def sum_of_squares(n):
    if is_one(n):
        return 1
    elif is_two(n):
        return 2
    elif is_three(n):
        return 3
    else:
        return 4  # Lagrange's four-square theorem
#  check better solution later on http://www.zrzahid.com/least-number-of-perfect-squares-that-sums-to-n/
