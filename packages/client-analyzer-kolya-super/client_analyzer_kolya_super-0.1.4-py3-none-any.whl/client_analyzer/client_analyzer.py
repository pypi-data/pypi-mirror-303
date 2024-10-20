import pandas as pd


class ClientAnalyzer:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.df = pd.read_csv(input_file)

        self.df['AgeGroup'] = self.df['age'].apply(self.agg_customer_age)

    def agg_customer_age(self, x):
        res = ""
        if x <= 25:
            res = "<=25"
        elif 25 < x <= 35:
            res = '26-35'
        elif 36 <= x <= 45:
            res = "36-45"
        elif 46 <= x <= 60:
            res = "46-60"
        else:
            res = ">60"

        return res

    def summarize_data(self):
        total_clients = len(self.df)
        grouped_by_age_group = self.df.groupby('AgeGroup')['age'].count()
        # grouped_by_age_group.rename(columns={'age': 'COUNT'}, inplace=True)

        grouped_by_city = self.df.groupby('city')['age'].count()
        # grouped_by_city.rename(columns={'age': 'COUNT'}, inplace=True)

        return total_clients, grouped_by_age_group, grouped_by_city

    def generate_report(self, output_file: str):
        total_clients, grouped_by_age_group, grouped_by_city = self.summarize_data()

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"TOTAL CLIENTS COUNT {total_clients}\n\n\n")
            file.write("Количество клиентов по возрастным группам\n")

            for item in grouped_by_age_group.items():
                file.write(f"{item[0]}: {item[1]}\n")

            file.write('Распределение клиентов по городам\n')
            for item in grouped_by_city.items():
                file.write(f"{item[0]} {item[1]}\n")

        print(f"Report saved in {output_file}")




