import argparse
from .calculation import landgroup

def main():
    parser = argparse.ArgumentParser(description="Анализ транзакций по категориям.")
    parser.add_argument('--input-file', required=True, help='Путь к входному файлу CSV.')
    parser.add_argument('--output-file', help='Путь к выходному файлу отчёта.')

    args = parser.parse_args()

    landgroup(args.input_file, args.output_file)

if __name__ == "__main__":
    main()