import argparse
from .analyzer import FinanceAnalyzer


def main():
    parser = argparse.ArgumentParser(description='Анализатор финансовых транзакций')
    parser.add_argument('--input-file', required=True, help='Путь к входному CSV-файлу')
    parser.add_argument('--output-file', required=True, help='Путь к выходному TXT-файлу')

    args = parser.parse_args()

    analyzer = FinanceAnalyzer(args.input_file)
    analyzer.generate_report(args.output_file)

if __name__ == "__main__":
    main()