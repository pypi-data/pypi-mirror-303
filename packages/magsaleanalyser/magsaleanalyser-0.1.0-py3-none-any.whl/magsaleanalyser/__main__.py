import argparse
from .report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="Sales Report Generator")
    parser.add_argument('--input-file', required=True, help="Input CSV file with sales data")
    parser.add_argument('--output-file', required=True, help="Output CSV file for the sales report")

    args = parser.parse_args()

    # Call the report generation function
    generate_report(args.input_file, args.output_file)

if __name__ == "__main__":
    main()