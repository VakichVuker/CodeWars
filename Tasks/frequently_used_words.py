from string import punctuation


def top_3_words(text):
    all_exclude_dict = list(punctuation.replace("'", ''))
    correct_string = text.lower()
    for symbol in all_exclude_dict:  # replace all punctuation symbols except "'"
        correct_string = correct_string.replace(symbol, ' ').replace('  ', ' ')
    counter_dict = {}
    for word in correct_string.split():  # count words
        if word.replace("'", ""):
            if counter_dict.get(word):
                counter_dict[word] += 1
            else:
                counter_dict[word] = 1
    return list(dict(sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)).keys())[:3]


if __name__ == '__main__':
    print(top_3_words(input()))
