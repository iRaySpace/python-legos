

def is_safe(numbers):
    temp = []
    for i in range(len(numbers) - 1):
        window_sum = numbers[i] - numbers[i + 1]
        temp.append(window_sum)
    # https://www.reddit.com/r/adventofcode/comments/1h4ncyr/comment/m0041k3/
    return set(temp) <= {1, 2, 3} or set(temp) <= {-1, -2, -3}


def is_safe_tolerant(numbers):
    for i in range(len(numbers)):
        adjusted_numbers = [x for idx, x in enumerate(numbers) if idx != i]
        if is_safe(adjusted_numbers):
            return True
    return False


def main():
    safe_numbers = 0
    unsafe_line_numbers = []
    with open('./res/2', 'r') as file:
        for line in file:
            numbers = [int(x) for x in line.strip().split(' ')]
            if is_safe(numbers):
                safe_numbers = safe_numbers + 1
            else:
                unsafe_line_numbers.append(numbers)
    print("Safe:", safe_numbers)

    tolerated_safe_numbers = 0
    for numbers in unsafe_line_numbers:
        if is_safe_tolerant(numbers):
            tolerated_safe_numbers = tolerated_safe_numbers + 1
    print("Tolerated:", tolerated_safe_numbers)

    print("Safe and tolerated:", safe_numbers + tolerated_safe_numbers)


if __name__ == '__main__':
    main()