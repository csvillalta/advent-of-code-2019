def is_valid(password: int):
    digits = [int(d) for d in password]
    has_adjacent = False
    i = 0
    while i < 5:
        if digits[i] > digits[i+1]:
            return False
        elif digits[i] == digits[i+1]:
            if i+2 <= 5 and digits[i] == digits[i+2]:
                i += 2
            elif i-1 >= 0 and digits[i] == digits[i-1]:
                i += 1
            else:
                has_adjacent = True
                i += 1
        else:
            i += 1
    return has_adjacent


def main():
    print(sum(is_valid(password) for password in range(136760, 595731)))


if __name__ == '__main__':
    main()