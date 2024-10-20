import pandas as pd


class FinanceAnalyzer:

    def __init__(self, csv_asset):
        self.csv_asset = csv_asset
        self.transactions = pd.read_csv(csv_asset)

    def summarize(self):
        income = self.transactions[self.transactions['category'] == 'Доход']
        expenses = self.transactions[self.transactions['category'] == 'Расход']

        total_income = income['amount'].sum()
        total_expenses = expenses['amount'].sum()

        return total_income, total_expenses

    def generate_report(self, output_file):
        total_income, total_expenses = self.summarize()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f'INCOME: {total_income}' + '\n')
            f.write(f"EXPENSES: {total_expenses}" + '\n')


