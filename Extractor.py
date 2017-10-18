import csv
import json


class Extractor:
    def __init__(self, _data, _csv):
        self.data = _data
        self.csv = _csv
        self.rates = []

    def extraction(self):
        self.data = json.loads(self.data)

        i = 0
        for rate in self.data:
            self.rates.append([])
            self.rates[i].append(rate['Cur_Name'])
            self.rates[i].append(rate['Cur_Scale'])
            self.rates[i].append(rate['Cur_OfficialRate'])
            i += 1

        self.__save_in_scv()

    def __save_in_scv(self):
        with open(self.csv, "w", newline='', encoding='utf8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for rate in self.rates:
                writer.writerow(rate)
