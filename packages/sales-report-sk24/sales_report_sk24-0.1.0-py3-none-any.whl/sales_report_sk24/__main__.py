import argparse
import pandas as pd
from .report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description='Generate sales report from CSV.')
    parser.add_argument('--input-file', required=True, help='Path to the input CSV file.')
    parser.add_argument('--output-file', required=True, help='Path to the output CSV file.')

    args = parser.parse_args()

    # Генерируем отчет
    report = generate_report(args.input_file)

    # Сохраняем отчет в CSV
    report.to_csv(args.output_file, index=False)

if __name__ == '__main__':
    main()