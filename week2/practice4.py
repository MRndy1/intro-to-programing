# Write a program that prompts the user to enter
# a number within the range of 1 through 10.
# The program should display the Roman numeral
# version of that number. If the number is outside
# the range of 1 through 10, the program should display
# an error message. The following table shows the Roman
# numerals for the numbers 1 through 10:

number = int(input("Enter a number between 1 through 10: \n"))

if number == 1:
    print(f"the roman numeral of {number} is I")
elif number == 2:
    print(f"the roman numberal of {number} is II")
elif number == 3:
    print(f"the roman numberal of {number} is III")
elif number == 4:
    print(f"the roman numberal of {number} is IV")
elif number == 5:
    print(f"the roman numberal of {number} is V")
elif number == 6:
    print(f"the roman numberal of {number} is VI")
elif number == 7:
    print(f"the roman numberal of {number} is VII")
elif number == 8:
    print(f"the roman numberal of {number} is VIII")
elif number == 9:
    print(f"the roman numberal of {number} is IX")
elif number == 10:
    print(f"the roman numberal of {number} is X")
else:
    print("please enter a number between 1 through 10")

