def remov_nb(n): # function
    all_variants = [x for x in range(1, n + 1)]
    sum_all = sum(all_variants)
    poss_pairs = []
    for num in all_variants:
        check_form = (sum_all - num) / (num + 1)
        if check_form.is_integer() and check_form in all_variants:
            poss_pairs.append((int(num), int(check_form)))
    return poss_pairs


if __name__ == '__main__':
    user_input = int(input())
    print(remov_nb(user_input))