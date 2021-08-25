def read_grades(n: int) -> list:
    grades = []
    for i in range(n):
        grade = float(input())
        grades.append(grade)
    return grades


def update_grade(grade: float, extra: float) -> (float, bool):
    extra_points = 2 if extra == 10 else 0
    new_grade = grade + extra_points
    new_grade = 10 if new_grade > 10 else new_grade
    changed = new_grade != grade

    return new_grade, changed


def change_grades(grades: list, second_chance: list) -> (list, int):
    new_grades = []
    total_changes = 0
    for i in range(len(grades)):
        grade, changed = update_grade(grades[i], second_chance[i])
        if changed:
            total_changes += 1
        new_grades.append((grades[i], grade, changed))
    return new_grades, total_changes


def run():
    n = int(input())

    grades = read_grades(n)
    second_chance = read_grades(n)

    updated_grades, updates = change_grades(grades, second_chance)

    print(f'NOTAS ALTERADAS: {updates}')
    for i in range(n):
        grade, final_grade, changed = updated_grades[i]
        print(f'{"*" if changed else "-"}({i+1:03d}) original: {grade:05.2f} | final: {final_grade:05.2f}')


if __name__ == '__main__':
    run()
