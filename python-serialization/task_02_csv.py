#!/usr/bin/python3
"""Module to convert CSV data into JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file into JSON format and save it as data.json.

    Returns:
        True if conversion was successful, False otherwise.
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError):
        return False
