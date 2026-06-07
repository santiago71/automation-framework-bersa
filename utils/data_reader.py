import csv
import json


def read_csv(file_path):

    with open(file_path, newline="") as csvfile:

        reader = csv.DictReader(csvfile)

        return list(reader)


def read_json(file_path):

    with open(file_path, encoding="utf-8") as file:

        return json.load(file)
