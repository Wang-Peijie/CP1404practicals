"""CP1404/CP5632 Practical - the client program of guitar."""
from guitar import Guitar
print("My guitars!")
guitars= []
name = input("Name:")
while name != "":
    year = int(input("Year:"))
    cost = float(input("Cost:"))
    guitar = Guitar(name, year, cost)
    print(f"{guitar} added.\n")
    guitars.append(guitar)
    name = input("Name:")
print("... snip ...\n\n")
print("These are my guitars:")


# test: guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
