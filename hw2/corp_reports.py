
import csv
import sys


INPUT_FILE = 'Corp_Summary.csv'
OUTPUT_FILE = 'department_summary.csv'


def read_employees() -> list[dict[str, str]]:
    """Читает данные сотрудников из CSV-файла."""
    with open(INPUT_FILE, encoding='utf-8-sig', newline='') as file:
        return list(csv.DictReader(file, delimiter=';'))


def show_hierarchy(employees: list[dict[str, str]]) -> None:
    """Выводит отделы каждого департамента."""
    departments: dict[str, set[str]] = {}
    for employee in employees:
        department = employee['Департамент']
        team = employee['Отдел']
        departments.setdefault(department, set()).add(team)

    for department, teams in sorted(departments.items()):
        print(department)
        for team in sorted(teams):
            print(f'  {team}')


def get_department_summary(
    employees: list[dict[str, str]],
) -> list[tuple[str, int, int, int, float]]:
    """Считает численность и зарплатные показатели по департаментам."""
    salaries: dict[str, list[int]] = {}
    for employee in employees:
        department = employee['Департамент']
        salary = int(employee['Оклад'])
        salaries.setdefault(department, []).append(salary)

    summary = []
    for department, amounts in sorted(salaries.items()):
        summary.append((
            department,
            len(amounts),
            min(amounts),
            max(amounts),
            round(sum(amounts) / len(amounts), 2),
        ))
    return summary


def show_department_summary(employees: list[dict[str, str]]) -> None:
    """Выводит зарплатную сводку по департаментам."""
    for department, count, minimum, maximum, average in get_department_summary(
            employees
    ):
        print(f'{department}: сотрудников — {count}, '
              f'мин. оклад — {minimum}, макс. оклад — {maximum}, '
              f'средний оклад — {average:.2f}')


def save_department_summary(employees: list[dict[str, str]]) -> None:
    """Сохраняет зарплатную сводку в CSV-файл."""
    with open(OUTPUT_FILE, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'Департамент', 'Количество сотрудников',
            'Минимальный оклад', 'Максимальный оклад', 'Средний оклад',
        ])
        writer.writerows(get_department_summary(employees))
    print(f'Отчёт сохранён в файл {OUTPUT_FILE}')


def main(variant: int) -> None:
    """Создаёт отчёт по выбранному номеру варианта."""
    if variant not in (1, 2, 3):
        print('Выберите вариант 1, 2 или 3')
        return

    employees = read_employees()
    if variant == 1:
        show_hierarchy(employees)
    elif variant == 2:
        show_department_summary(employees)
    else:
        save_department_summary(employees)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Запуск: python corp_reports.py <номер варианта>')
    else:
        try:
            main(int(sys.argv[1]))
        except ValueError:
            print('Номер варианта должен быть целым числом')
