

def get_total_distance(left_numbers, right_numbers):
    distances = [abs(left - right) for left, right in zip(left_numbers, right_numbers)]
    return sum(distances)


def get_similarity_score(left_numbers, right_numbers):
    total_similarity_score = 0
    existing_counts = {}
    for left in left_numbers:
        if left not in existing_counts:
            existing_counts[left] = right_numbers.count(left)
        similarity_score = left * existing_counts.get(left)
        total_similarity_score = total_similarity_score + similarity_score
    return total_similarity_score


def main():
    left_numbers = []
    right_numbers = []

    with open('./res/1', 'r') as file:
        for line in file:
            stripped_line = line.strip()
            left, right = stripped_line.split('   ')
            left_numbers.append(int(left))
            right_numbers.append(int(right))

    left_numbers = sorted(left_numbers)
    right_numbers = sorted(right_numbers)

    print(get_total_distance(left_numbers, right_numbers))
    print(get_similarity_score(left_numbers, right_numbers))


if __name__ == '__main__':
    main()
