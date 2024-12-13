

def is_safe(numbers):
    polarity = None

    for i in range(len(numbers) - 1):
        window_sum = numbers[i] - numbers[i + 1]

        if window_sum == 0 or abs(window_sum) > 3:
            return False

        if window_sum > 0:
            if polarity == -1: return False
            polarity = 1
        else:
            if polarity == 1: return False
            polarity = -1

    return True


def main():
    safe_numbers = 0
    line_numbers = []
    with open('./res/2', 'r') as file:
        for line in file:
            line = line.strip()
            numbers = [int(x) for x in line.split(' ')]
            if is_safe(numbers):
                safe_numbers = safe_numbers + 1
            line_numbers.append(numbers)


if __name__ == '__main__':
    main()
