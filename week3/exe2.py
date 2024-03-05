# Exercise 2:
#
# Running on a particular treadmill
# you burn 4.2 calories per minute.
# Write a program that
# uses a loop to display the number
# of calories burned after
# 10, 15, 20, 25, and 30 minutes.
per_minute = 4.2

for i in range(10,30,5):
    total = i * per_minute
    print(f"in {i} minutes the total cal you burn is {total} cal")

