#total purchase
item1 = input("enter the price of item 1\n")
item2 = input("enter the price of item 2\n")
item3 = input("enter the price of item 3\n")
item4 = input("enter the price of item 4\n")
item5 = input("enter the price of item 5\n")

item1_int = int(item1)
item2_int = int(item2)
item3_int = int(item3)
item4_int = int(item4)
item5_int = int(item5)

subtotal = item1_int + item2_int + item3_int + item4_int + item5_int

print("subtotal: ",subtotal)
tax = subtotal * 0.07
print("tax: ",tax)
total = subtotal + tax
print("total: ",total)