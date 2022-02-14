import csv

with open('phones.csv', encoding='utf-8') as file:
    reader_object = csv.reader(file, delimiter=";")
    reader = csv.DictReader(file, delimiter=";")
    for raw in reader:
        print(raw['name'])
