import string


class RockConcert:
    moshpits_position_diff = [[0, 1], [1, 0], [1, 1]]

    def __init__(self, dance_floor, places_symbol='?'):
        self.dance_floor = [list(raw) for raw in dance_floor]
        self.best_place = (-1, -1)
        self.places_symbol = places_symbol

    def print_dance_floor(self):
        for raw in self.dance_floor:
            print("'" + ''.join(raw) + "',")

    def analyze_concert(self):
        for raw in range(0, len(self.dance_floor)-1):
            for column in range(0, len(self.dance_floor[raw])-1):
                if self.dance_floor[raw][column] == " ":
                    count_spaces_around = [self.dance_floor[raw + i][column + j]
                                           for i, j in RockConcert.moshpits_position_diff
                                           if self.dance_floor[raw + i][column + j] == ' ']
                    if len(count_spaces_around) == 3:
                        self.mark_whole_moshpit_recursive(raw, column)
        else:
            count_spaces = sum([raw.count(' ') for raw in self.dance_floor])
            if count_spaces == 0:
                self.places_symbol = '?'
            else:
                self.places_symbol = ' '

    def mark_whole_moshpit_recursive(self, y, x):
        self.dance_floor[y][x] = '?'
        moshpits_concatenates = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for i, k in moshpits_concatenates:
            if 0 <= y + i < len(self.dance_floor) and 0 <= x + k < len(self.dance_floor[y]):
                if self.dance_floor[y + i][x + k] and self.dance_floor[y + i][x + k] == ' ':
                    self.mark_whole_moshpit_recursive(y + i, x + k)

    def find_best_place(self):
        all_pos_dict = {}
        for raw in range(0, len(self.dance_floor)):
            for column in range(0, len(self.dance_floor[raw])):
                if self.dance_floor[raw][column] == self.places_symbol:
                    all_pos_dict[(raw, column)] = self.calculate_place_point(raw, column)
        sorted_tuples = sorted(all_pos_dict.items(), key=lambda item: item[1], reverse=True)
        self.best_place = sorted_tuples[0][0]

    def calculate_place_point(self, raw, column):
        result_points = len(self.dance_floor) - raw
        if raw > 0:
            men_in_front = str(self.dance_floor[raw-1][column]).lower()
            result_points *= 0.99 ** (list(self.places_symbol + string.ascii_letters).index(men_in_front))
        for near_diff_raw, near_diff_column in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            if 0 <= (column + near_diff_column) < len(self.dance_floor[raw]) and 0 <= (raw + near_diff_raw) < len(self.dance_floor):
                near_men = self.dance_floor[raw + near_diff_raw][column + near_diff_column]
                if near_men in list(string.ascii_uppercase):
                    result_points = result_points * 0.8
        return result_points


def best_place(dance_floor):
    new_rock_concert = RockConcert(dance_floor=dance_floor)
    new_rock_concert.analyze_concert()
    new_rock_concert.find_best_place()
    return new_rock_concert.best_place


if __name__ == '__main__':
    user_dance_floor = [
    'kbfvXiefReFmdhu ',
    'flsyx zwF  jc n ',
    'znymt SjqheOxgor',
    'BnV jwHnLt?????z',
    'gtdfbtxqoq?????h',
    'HwikBkUyqz?????X',
    'BFlroxe pZBalGpz',
    ]
    print(best_place(user_dance_floor))

