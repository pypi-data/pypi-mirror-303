import argparse
from .client_analyzer import ClientAnalyzer


def main():
    parser = argparse.ArgumentParser("Client Analizer package")
    parser.add_argument('--input-file', required=True)
    parser.add_argument("--output-file", required=True)

    args = parser.parse_args()
    reporter = ClientAnalyzer(args.input_file)
    reporter.generate_report(args.output_file)


if __name__ == '__main__':
    main()
