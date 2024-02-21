import math
# Assume hot dogs come in packages of 10, and hot dog
# buns come in packages of 8. Write a program that calculates
# the number of packages of hot dogs and the number of packages
# of hot dog buns needed for a cookout, with the minimum amount
# of leftovers. The program should ask the user for the number
# of people attending the cookout and the number of hot dogs each
# person will be given. The program should display the following details:
#
# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over

people = int(input("How many people will be attending to eat hotdog: \n"))
hotdog_each_person = int(input("How many hotdog do you wanna give for each person: \n"))

one_hotdog_package = 10
one_bun_package = 8

hotdog_needed = people * hotdog_each_person
hotdog_package_needed = math.ceil(hotdog_needed / one_hotdog_package)
hotdog_leftover = (hotdog_package_needed * one_hotdog_package) - hotdog_needed

bun_package_needed = math.ceil(hotdog_needed / one_bun_package)
bun_leftover = (bun_package_needed * one_bun_package) - hotdog_needed

print(f"the minimum number of packages of hotdogs required is {hotdog_package_needed} package")
print(f"the minimum number of packages of hotdogs buns required is {bun_package_needed} package")
print(f"the number of hotdogs that will be left over is {hotdog_leftover} hotdog")
print(f"the number of hotdog buns that will be left over is {bun_leftover} buns ")


