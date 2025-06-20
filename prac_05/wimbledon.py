"""
CP1404_prac05
Write a program to read this file, process the data and display processed information
Estimate: 20 minutes
Actual:
"""
FILENAME = "wimbledon.csv"
def main():
    champion_names = []
    countrys = []
    wimbledon_data = read_file()
    # print(wimbledon_data)
    for line in wimbledon_data:
        champion_names.append(line.strip().split(",")[2])
        countrys.append(line.strip().split(",")[3])
    # print(champion_names)
    # print(countrys)
    countrys = organize_countrys(countrys)

def calculate_champion_times(data):
    pass

def read_file():
    #read file lines in to a list
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = in_file.readlines()
    return data

def organize_countrys(data):
    data = set(data)
    # print(data)
    return sorted(list(data))
main()