import argparse
from .bill_manager import BillManager


def main():
    parser = argparse.ArgumentParser("Bill report genereator")
    parser.add_argument('--input-file', required=True)
    parser.add_argument("--output-file", required=True)

    args = parser.parse_args()
    reporter = BillManager(args.input_file)
    reporter.generate_report(args.output_file)


if __name__ == '__main__':
    main()
