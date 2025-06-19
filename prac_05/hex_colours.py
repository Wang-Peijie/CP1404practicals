"""
Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get the code
Estimate: 10 minutes
Actual:   13 minutes
"""
NAME_TO_COLOR = {"Army Green": "#4b5320", "Baby Blue": "#89cff0", "Amethyst": "#9966cc", "Aqua": "#00ffff",
                  "Aureolin": "#fdee00",
                  "Barn Red": "#7c0a02", "Beaver": "#9f8170", "Bistre": "#3d2b1f", "Bole": "#79443b", "Bone": "#e3dac9",
                  "Camel": "#c19a6b", }
color_name = input("Enter color name: ").title()
while color_name != '':
    try:
        print(color_name, "code is", NAME_TO_COLOR[color_name])
    except KeyError:
        print("Invalid color name!")
    color_name = input("Enter color name: ").title()
