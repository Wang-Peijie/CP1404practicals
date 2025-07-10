"""
CP1404/CP5632 Practical - myguitars
Estimated time:30min
Actual time:40min
"""
from guitar import Guitar
import csv

FILENAME = "guitars.csv"


def main():
    """Show guitar information and store new data into CSV."""
    csv_data = read_file()
    guitars = convert_list_to_objects_list(csv_data)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    print("Enter a new guitar:")
    name = input("Enter it's name:")
    year = int(input("Production Date："))
    cost = float(input("How much:"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name},{year},{cost}")
    store_data_in_csv_file(guitars)


def read_file():
    """Read data from CSV file and return list"""
    data = []
    with open(FILENAME, "r", encoding='utf-8') as in_file:
        lines = list(csv.reader(in_file))
        for line in lines:
            data.append(line)
            # print(line)
    # print(data)
    return data


def convert_list_to_objects_list(data):
    """Convert list of [name, year, cost] to list of Guitar objects"""
    guitars = []
    for parts in data:
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitars.append(Guitar(name, year, cost))
    return guitars


def store_data_in_csv_file(data):
    """store data to the CSV file."""
    with open(FILENAME, "w", encoding="utf-8") as out_file:
        write = csv.writer(out_file)
        for parts in data:
            write.writerow(parts)


main()
