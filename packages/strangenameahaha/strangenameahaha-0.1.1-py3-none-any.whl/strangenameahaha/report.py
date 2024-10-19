import csv
import os
from collections import defaultdict

def load_customers(input_file: str):
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Файл {input_file} не найден.")

    customers = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            customers.append(row)
    
    return customers

def generate_report(customers):
    total_customers = len(customers)

    age_groups = defaultdict(int)
    city_distribution = defaultdict(int)

    for customer in customers:
        # Обработка возрастной группы
        age = int(customer['age'])
        if 18 <= age <= 25:
            age_groups['18-25'] += 1
        elif 26 <= age <= 35:
            age_groups['26-35'] += 1
        elif 36 <= age <= 45:
            age_groups['36-45'] += 1
        elif 46 <= age <= 60:
            age_groups['46-60'] += 1

        # Обработка города
        city = customer['city']
        city_distribution[city] += 1

    report_lines = [
        f"Общее количество клиентов: {total_customers}\n\n",
        "Количество клиентов по возрастным группам:\n"
    ]

    for group, count in age_groups.items():
        report_lines.append(f"{group}: {count}\n")

    report_lines.append("\nРаспределение клиентов по городам:\n")
    for city, count in city_distribution.items():
        report_lines.append(f"{city}: {count}\n")

    return ''.join(report_lines)

def save_report(output_file: str, report: str):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Отчет успешно создан: {output_file}")
