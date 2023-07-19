def round_grade(grade):
    if grade < 40:
        return grade
    grade_fifth_multiple = (grade + 5) - (grade % 5)
    if (grade_fifth_multiple - grade) >= 3:
        return grade
    else:
        return grade_fifth_multiple


def main():
    grades_len = int(input().strip())
    grades = [int(input().strip()) for x in range(grades_len)]
    rounded_grade = [round_grade(x) for x in grades]
    print(rounded_grade)

if __name__ == "__main__":
    main()
