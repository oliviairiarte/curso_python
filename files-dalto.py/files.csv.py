
import csv

with open("data2.csv") as file: #sin libreria pandas
    reader = csv.reader(file)
    for row in reader:
        print(row)

