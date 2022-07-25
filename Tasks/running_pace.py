
def running_pace(distance, time):
    m, s = map(int, time.split(':'))
    second = m * 60 + s
    pace = second / distance
    return f'{int(pace // 60)}:{int(pace % 60):02}'


if __name__ == '__main__':
    running_pace(float(input()), input())