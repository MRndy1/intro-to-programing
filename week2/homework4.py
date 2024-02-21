# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
# •Pocket 0 is green.
# For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
# For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red.
# For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black.
# For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red.
#
# Write a program that asks the user to enter a pocket number and displays whether the pocket is green,
# red, or black. The program should display an error message if the user enters a number that is outside
# the range of 0 through 36.

pocket_number = int(input("Enter the pocket number between 0 through 36: \n"))

if pocket_number == 0:
    print(f"the pocket number {pocket_number} is green")
elif pocket_number >= 1 and pocket_number <= 10:
    if pocket_number % 2 == 0:
        print(f"the pocket number {pocket_number} is black")
    else:
        print(f"the pocket number {pocket_number} is red")
elif pocket_number >= 11 and pocket_number <= 18:
    if pocket_number % 2 == 0:
        print(f"the pocket number {pocket_number} is red")
    else:
        print(f"the pocket number {pocket_number} is black")
elif pocket_number >= 19 and pocket_number <= 28:
    if pocket_number % 2 == 0:
        print(f"the pocket number {pocket_number} is black")
    else:
        print(f"the pocket number {pocket_number} is red")
elif pocket_number >= 29 and pocket_number <= 36:
    if pocket_number % 2 == 0:
        print(f"the pocket number {pocket_number} is red")
    else:
        print(f"the pocket number {pocket_number} is black")
else:
    print("invalid input please enter a number between 0 through 36")

