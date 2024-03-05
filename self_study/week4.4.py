# Q4. Write a program that asks the user to enter
# the monthly costs for the following expenses
# incurred from operating his or her automobile:
# loan payment, insurance, gas, oil, tires, and
# maintenance. The program should then display
# the total monthly cost of these expenses,
# and the total annual cost of these expenses.


automobile = int(input("please enter your automobile monthly expenses: \n"))
loan = int(input("please enter your loan monthly expenses: \n"))
insurance  = int(input("please enter your insurance monthly expenses: \n"))
gas = int(input("please enter your gas monthly expenses: \n"))
oil = int(input("please enter your oil monthly expenses: \n"))
tires = int(input("please enter your tires monthly expenses: \n"))
maintenance = int(input("please enter your maintenance monthly expenses: \n"))

def monthly_expenses():
    monthly = automobile + loan + insurance + gas + oil + tires + maintenance
    return monthly

def annual_cost():
    annual = monthly_expenses() * 12
    return annual

print(f"your total monthly cost is ${monthly_expenses()}")
print(f"your annual cost is ${annual_cost()}")

