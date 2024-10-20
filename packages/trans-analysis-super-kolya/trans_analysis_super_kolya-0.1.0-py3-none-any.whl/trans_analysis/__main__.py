import argparse
from .analyzer import FinanceAnalyzer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', required=True)
    parser.add_argument('--output-file', required=True)

    args = parser.parse_args()

    analyzer = FinanceAnalyzer(args.input_file)
    analyzer.generate_report(args.output_file)


if __name__ == '__main__':
    main()
