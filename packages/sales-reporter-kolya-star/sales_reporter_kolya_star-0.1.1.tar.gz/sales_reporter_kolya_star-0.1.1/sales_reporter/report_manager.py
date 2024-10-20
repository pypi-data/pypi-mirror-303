import pandas as pd


class ReportManager:

    def __init__(self, input_file: str):
        self.input_file = input_file
        self.sales = pd.read_csv(input_file)

    def summary_data(self):
        groped_by_category = self.sales.groupby('category').sum().reset_index()
        return groped_by_category

    def generate_report(self, output_file: str):
        df = self.summary_data()
        df.to_csv(output_file, index=False, encoding='utf-8')

        print(f"File saved in {output_file}!")

