colors = ['Blue', 'Yellow', 'Black', 'Red', 'White']
favorite_color = input("What is your favorite color? ")

if favorite_color in colors:
    index = colors.index(favorite_color)
    print(f"Your color is at index {index} in my list")
else:
    print("Sorry, I could not find your color")