import csv

with open("file.csv", "r") as data_file:
    csv_data = csv.DictReader(data_file)

