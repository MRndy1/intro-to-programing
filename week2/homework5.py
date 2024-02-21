# Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar.
# The program should prompt the user to enter the number of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar,
# the program should congratulate the user for winning the game.
# Otherwise, the program should display a message indicating whether
# the amount entered was more than or less than one dollar.

pennies = 1
nickels = 5
dimes = 10
quarters = 25
dollar = 100
print("""
this is a change-counting game
you must count how many pennies,nickels,dimes,and quarters eqSual to one dollar
""")
player_pennies = int(input("How many pennies do you wanna insert: \n"))
player_nickels = int(input("How many pennies do you wanna insert: \n"))
player_dimes = int(input("How many pennies do you wanna insert: \n"))
player_quarters = int(input("How many pennies do you wanna insert: \n"))

player_total = (player_pennies * pennies) + (player_nickels * nickels) + (player_dimes * dimes) + (player_quarters * quarters)

if player_total == dollar:
    print("You won! that's exactly the value of 1 dollar")
elif player_total > dollar:
    print("You Lose! the ammount you inserted is more than the value of 1 dollar")
else:
    print("You Lose! the ammount you inserted is less than the value of 1 dollar")
