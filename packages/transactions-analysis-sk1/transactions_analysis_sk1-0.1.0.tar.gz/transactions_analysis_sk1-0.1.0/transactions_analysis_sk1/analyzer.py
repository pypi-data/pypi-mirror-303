import pandas as pd


class FinanceAnalyzer:
    def __init__(self, input_file):
        self.input_file = input_file
        self.transactions = pd.read_csv(input_file)

    def summarize(self):
        income = self.transactions[self.transactions['category'] == 'Доход']
        expenses = self.transactions[self.transactions['category'] == 'Расход']

        total_income = income['amount'].sum()
        total_expenses = expenses['amount'].sum()

        return total_income, total_expenses

    def generate_report(self, output_file):
        total_income, total_expenses = self.summarize()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Доход: {total_income} руб.\n")
            f.write(f"Расход: {total_expenses} руб.\n")