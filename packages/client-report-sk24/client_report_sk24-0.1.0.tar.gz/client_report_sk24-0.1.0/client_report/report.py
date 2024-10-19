import csv
from collections import Counter


class ClientReport:
    def __init__(self, input_file):
        self.clients = self.load_data(input_file)

    def load_data(self, input_file):
        clients = []
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                clients.append(row)
        return clients

    def generate_report(self):
        total_clients = len(self.clients)
        age_groups = self.get_age_distribution()
        cities = self.get_city_distribution()

        report = f"Общее количество клиентов: {total_clients}\n\n"
        report += "Количество клиентов по возрастным группам:\n"
        for age_group, count in age_groups.items():
            report += f"{age_group}: {count}\n"

        report += "\nРаспределение клиентов по городам:\n"
        for city, count in cities.items():
            report += f"{city}: {count}\n"

        return report

    def get_age_distribution(self):
        age_bins = {
            '18-25': 0,
            '26-35': 0,
            '36-45': 0,
            '46-60': 0,
            '60+': 0,
        }
        for client in self.clients:
            age = int(client['age'])
            if age <= 25:
                age_bins['18-25'] += 1
            elif age <= 35:
                age_bins['26-35'] += 1
            elif age <= 45:
                age_bins['36-45'] += 1
            elif age <= 60:
                age_bins['46-60'] += 1
            else:
                age_bins['60+'] += 1
        return age_bins

    def get_city_distribution(self):
        cities = Counter(client['city'] for client in self.clients)
        return cities
