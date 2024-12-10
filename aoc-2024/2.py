def is_safe(numbers):
    current_number = next(iter(numbers))


def main():
    numbers = []
    with open('./res/2', 'r') as file:
        for line in file:
            line = line.strip()
            numbers = [int(x) for x in line.split(' ')]
            print(is_safe(numbers))


if __name__ == '__main__':
    main()
