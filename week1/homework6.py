purchase = input("enter the amount of a purchase : \n")
instalments = input("enter the desired number of payment instalments: \n")
purchase_int = int(purchase)
instalments_int = int(instalments)
tax = purchase_int * 0.05
end_price = tax + purchase_int
per_month = end_price / instalments_int
print("the total amount of the purchase is", end_price)
print("the instalment cost per month is", per_month, "for",instalments,"month")
