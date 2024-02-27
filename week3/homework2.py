from prettytable import PrettyTable
# Exercise 7:
#
# Write a program that calculates the amount
# of money a person would earn over a period
# of time if his or her salary is one penny the
# first day, two pennies the second day, and
# continues to double each day. The program
# should ask the user for the number of days.
# Display a table showing what the salary was
# for each day, then show the total pay at the
# end of the period. The output should be
# displayed in a dollar amount, not the
# number of pennies.
salary = 1
days = int(input("How many days do you wanna calculates: \n")) + 1
table = PrettyTable()
table.field_names = ["Days", "Salary"]
table.add_row(["1", "0.01$"])
for i in range(2,days):
    salary *= 2
    total = salary / 100
    table.add_row([i, f"{total}$"])

print(table)