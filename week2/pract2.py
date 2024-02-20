# Exercise 2:
#
# The area of a rectangle is the rectangle’s length times its width.
# Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area,
# or if the areas are the same.

length1 = int(input("Enter the first length of the rectangle: \n"))
width1 = int(input("Enter the first width of the rectangle: \n"))

length2 = int(input("Enter the second length of the rectangle: \n"))
width2 = int(input("Enter the second width of the rectangle: \n"))

rectangle1 = width1 * length1
rectangle2 = width2 * length2

if rectangle1 == rectangle2:
    print(f"the area of both rectangle is {rectangle1}")
elif rectangle1 > rectangle2:
    print("the area of the first rectangle is greater than the second rectangle")
elif rectangle1 < rectangle2:
    print("the area of the first rectangle is smaller than the second rectangle")
else:
    print("please enter the right number")
    

