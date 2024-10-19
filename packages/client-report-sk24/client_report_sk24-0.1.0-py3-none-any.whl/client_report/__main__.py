import argparse
from .report import ClientReport


def main():
    parser = argparse.ArgumentParser(description='Generate client report from CSV data.')
    parser.add_argument('--input-file', required=True, help='Path to input CSV file.')
    parser.add_argument('--output-file', required=True, help='Path to output TXT file.')

    args = parser.parse_args()

    report_generator = ClientReport(args.input_file)
    report = report_generator.generate_report()

    with open(args.output_file, 'w', encoding='utf-8') as file:
        file.write(report)

if __name__ == '__main__':
    main()