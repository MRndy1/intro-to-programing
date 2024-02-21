# A class has two tests worth 25 points each along with a
# main exam worth 50 points. For a student to pass the class,
# they must obtain an overall score of at least 50 points and
# must obtain at least 25 points in the main exam. If a student’s
# total score is less than 50 or they obtain less than 25 points
# in the main exam, they receive a grade of “Fail”. Otherwise,
# their grade is as follows:
#
# If they get more than 80, they get a grade of “Distinction”.
# 50–59 = “Pass”.
# If they get less than 80 but more than 60, they get a “Credit” grade.
# If they get less than 60, they get a “Pass” grade.
#
# Write a program that prompts the user to enter their points
# for both tests and the exam and converts the values to integers.
# The program should first check if the points entered for the tests
# and exam are valid. If any of the test scores are not between 0 and 25,
# or the exam score is not between 0 and 50, the program should display
# an error message. Otherwise, the program should display the total
# points and the grade.

first_test = int(input("Please enter your first test grade between 0 and 25: \n"))
second_test = int(input("Please enter your second test grade between 0 and 25: \n"))
main_test = int(input("Please enter your main test grade between 0 and 50: \n"))

overall_test = first_test + second_test + main_test

if overall_test >= 50 and main_test >= 25:
    if overall_test > 80:
        print ("Distinction")
    elif overall_test >=60 and overall_test <= 80:
        print ("Credit")
    elif overall_test >=50 and overall_test < 60:
        print ("pass")
else:
    print("you fail")
