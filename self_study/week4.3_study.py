# Q3. Many financial experts advise that property owners
# should insure their homes or buildings
# for at least 80 percent of the amount it would cost
# to replace the structure. Write a program
# that asks the user to enter the replacement cost dd
# of a building, then displays the minimum
# amount of insurance he or she should buy for the property.

replacement_cost = int(input("please enter your replacement cost: \n"))

def insurance():
    insurance_cost = replacement_cost * 0.8
    return insurance_cost
print(f"your minimum insurance cost is: {insurance()}")