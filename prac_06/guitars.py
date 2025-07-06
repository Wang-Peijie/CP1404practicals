"""CP1404/CP5632 Practical - the client program of guitar."""
from guitar import Guitar

CURRENT_YEAR = 2025
print("My guitars!")
guitars= []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    print(f"{guitar} added.\n")
    guitars.append(guitar)
    name = input("Name: ")
print("\n... snip ...\n")
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
# for test: guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
