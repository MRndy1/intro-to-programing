# Write a program that asks the
# user to enter a distance in
# kilometers, then converts that
# distance to miles.
# The conversion formula is as follows:
# Miles = Kilometers 3 0.6214

km = int(input("Enter a distance in kilometers: "))
def miles(km):
    convert = km * 0.621371
    return convert
print(f"The distance in miles is {miles(km)} miles")