import pandas as pd

def generate_report(input_file, output_file):
    # Load the sales data from CSV
    df = pd.read_csv(input_file)

    # Group by 'category' and calculate total sales and quantity sold
    report = df.groupby('category').agg(
        sales=('sales', 'sum'),
        quantity=('quantity', 'sum')
    ).reset_index()

    # Save the report to CSV
    report.to_csv(output_file, index=False)
