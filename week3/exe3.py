# Exercise 3:
#
# Write a program that asks the user to enter the number of times
# that they have run around
# a racetrack, and then uses a loop to prompt them to enter the
# lap time for each of their laps.
# When the loop finishes, the program should display the time of
# their fastest lap, the time of
# their slowest lap, and their average lap time.

number_of_times = int(input("How many times do you have run around a racetrack: \n"))
number_of_time_plus = number_of_times + 1
total_lap_time = 0
collection_lap_time = int()
for time in range(1,number_of_time_plus):
    lap_time = float(input(f"enter lap time {time}: \n"))

    total_lap_time += lap_time
    average = total_lap_time/number_of_times
fastest_lap = min(lap_time)
slowest_lap = min(lap_time)
print(fastest_lap, slowest_lap, average)



