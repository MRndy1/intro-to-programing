food_charge = input("please enter the total amount of a meal you have been purchased at the restaurant: \n")
tip = int(food_charge) * 0.18
tax = int(food_charge) * 0.07
total = int(food_charge) + tip + tax
print("tips:",int(tip))
print("tax:",int(tax))
print("total:",int(total))