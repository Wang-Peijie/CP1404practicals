"""CP1404/CP5632 Practical - myguitars"""
from guitar import Guitar
import csv

FILENAME = "guitars.csv"

def main():
    """"""
    csv_data = read_file()
    guitars = convert_list_to_objects_list(csv_data)
    # print(guitars)


def read_file():
    """Read data from CSV file and return list"""
    data = []
    with open(FILENAME,"r",encoding='utf-8') as in_flie:
        lines = list(csv.reader(in_flie))
        for line in lines:
            data.append(line)
            # print(line)
    print(data)
    return data

def convert_list_to_objects_list(data):
    """Convert list of [name, year, cost] to list of Guitar objects"""
    guitars = []
    for parts in data:
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitars.append(Guitar(name,year,cost))
    return guitars

main()