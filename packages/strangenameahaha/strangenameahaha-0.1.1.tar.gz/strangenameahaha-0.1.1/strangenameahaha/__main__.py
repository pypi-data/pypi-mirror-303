import argparse
from .report import load_customers, generate_report, save_report

def main():
    parser = argparse.ArgumentParser(description='Генерация отчета о клиентах.')
    parser.add_argument('--input-file', required=True, help='Путь к входному файлу .csv с данными о клиентах.')
    parser.add_argument('--output-file', required=True, help='Путь к выходному файлу .txt для сохранения отчета.')

    args = parser.parse_args()

    customers = load_customers(args.input_file)
    report = generate_report(customers)
    save_report(args.output_file, report)

if __name__ == '__main__':
    main()
