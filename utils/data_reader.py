import csv
import json


def read_csv(file_path):

<<<<<<< HEAD
    data = []

    with open(file_path, newline="", encoding="utf-8") as csvfile:
=======
    with open(file_path, newline="") as csvfile:
>>>>>>> 0f9283e4534d9b48374b38c66ecf84388efd46ef

        reader = csv.DictReader(csvfile)

        return list(reader)

<<<<<<< HEAD
            data.append(
                (
                    row["username"],
                    row["password"],
                    row["expected"] == "True",
                    row["error_message"],
                )
            )
=======
>>>>>>> 0f9283e4534d9b48374b38c66ecf84388efd46ef

def read_json(file_path):

    with open(file_path, encoding="utf-8") as file:

        return json.load(file)
