def is_valid(password: int):
    digits = [int(d) for d in password]
    has_adjacent = False
    for i in range(5):
        if digits[i] > digits[i+1]:
            return False
        elif digits[i] == digits[i+1]:
            has_adjacent = True
    return has_adjacent


def main():
    print(sum(is_valid(password) for password in range(136760, 595731)))


if __name__ == '__main__':
    main()