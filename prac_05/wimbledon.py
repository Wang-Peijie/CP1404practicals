"""
CP1404_prac05
Write a program to read this file, process the data and display processed information
Estimate: 20 minutes
Actual:
"""
FILENAME = "wimbledon.csv"
def main():
    wimbledon_data = read_file()
    print(wimbledon_data)

def calculate_total_times(data):
    pass

def read_file():
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = in_file.readlines()
    return data

def store_country(data):
    pass

main()