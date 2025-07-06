"""CP1404/CP5632 Practical - guitar tast."""
from guitar import Guitar

CURRENT_YEAR = 2025

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 10000.00)

print(f"{guitar1.name} get_age() - Expected 103. Got {guitar1.get_age(CURRENT_YEAR)}")
print(f"{guitar2.name} get_age() - Expected 12. Got {guitar2.get_age(CURRENT_YEAR)}")
