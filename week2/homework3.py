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

people = int(input("How many people"))
hotdog_each_person = int(input("How many hotdog do you wanna give per each person"))

one_hotdog_package = 10
one_bun_package = 8

hotdog_needed = people * hotdog_each_person
hotdog_package_needed = hotdog_needed / one_hotdog_package
rounded_hotdog_package = math.ceil(hotdog_package_needed)
left_over_hotdog = int((rounded_hotdog_package - hotdog_package_needed) * 10)

bun_package_needed = hotdog_needed / one_bun_package
rounded_bun_package = math.ceil(bun_package_needed)
left_over_bun = int((rounded_bun_package - bun_package_needed) * 10)

print(left_over_bun)
