import csv

with open("genarator-settings.csv", "r")as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        print(line)