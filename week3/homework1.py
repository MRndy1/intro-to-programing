from prettytable import PrettyTable
# Exercise 6:
#
# Write a program that displays a table of distances
# in miles and their equivalent distances in
# kilometers, rounded to 2 decimal places.
# One mile is equivalent to 1.60934 kilometers.
# The table should be generated using a loop and
# should include values in 10 mile increments
# from 10 to 80.
table = PrettyTable()
table.field_names = ["miles", "kilometers"]

for mile in range(10,81,10):
    km = 1.60934
    convert_km = round(mile * km, 2)
    table.add_row([mile,convert_km])
print(table)
