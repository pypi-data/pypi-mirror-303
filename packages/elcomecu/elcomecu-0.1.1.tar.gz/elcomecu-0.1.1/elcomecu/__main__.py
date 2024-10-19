import argparse
from .receipt import generate_receipt

def main():
    parser = argparse.ArgumentParser(description='Генерация чека на основе данных о заказе.')
    parser.add_argument('--input-file', required=True, help='Путь к входному файлу .json с данными о заказе.')
    parser.add_argument('--output-file', required=True, help='Путь к выходному файлу .txt для сохранения чека.')

    args = parser.parse_args()

    generate_receipt(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
