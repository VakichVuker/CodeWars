def sum_array(arr):
    return sum(arr) - (min(arr) + max(arr)) if arr and len(arr) > 1 else 0


if __name__ == '__main__':
    user_input = [int(x) for x in input().split()]
    print(sum_array(user_input))
