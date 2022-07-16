def int32_to_ip2(int32):
    return '.'.join([str((int32 & (255 << mask)) >> mask) for mask in range(24, -1, -8)])


if __name__ == '__main__':
    print(int32_to_ip2(int(input())))