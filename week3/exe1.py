# Exercise 1:
# A bug collector collects bugs every day for five days.
# Write a program that keeps a running
# total of the number of bugs collected during the five days.
# The loop should ask for the
# number of bugs collected for each day,
# and when the loop is finished, the program should
# display the total number of bugs collected.
t_bugs = 0
for day in range(1, 6):
    bugs = int(input(f"how many bugs do you catch in day {day}: \n"))
    t_bugs += bugs
print(f"the total bugs is: {t_bugs}")

