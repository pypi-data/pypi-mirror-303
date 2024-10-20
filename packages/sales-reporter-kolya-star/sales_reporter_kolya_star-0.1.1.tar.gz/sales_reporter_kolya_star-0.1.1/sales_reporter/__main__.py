import argparse
from .report_manager import ReportManager


def main():
    parser = argparse.ArgumentParser("Sales reporter")
    parser.add_argument('--input-file', required=True)
    parser.add_argument("--output-file", required=True)

    args = parser.parse_args()
    reporter = ReportManager(args.input_file)
    reporter.generate_report(args.output_file)


if __name__ == '__main__':
    main()
