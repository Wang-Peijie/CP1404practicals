'''
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
'''
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    number_of_items = int(input("Number of items must be greater than 0. Please enter a valid number: "))
total_price = 0
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    discount = 0.1 * total_price
    total_price -= discount
print(f"Total price for {number_of_items} is: ${total_price}")