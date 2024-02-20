cyber = int(input("Enter uour cyber grade: "))
python = int(input("Enter uour python grade: "))
networking = int(input("Enter uour networking grade: "))

avg = (cyber + python + networking) / 3

if avg >= 90:
    print(f"your grade is {avg} and its a higher distinction")
elif avg >= 75 and avg <= 90:
    print(f"your grade is {avg} and its a distinction")
elif avg >= 60 and avg < 75:
    print(f"your grade is {avg} and its a credit")
elif avg >= 50 and avg < 60:
    print(f"your grade is {avg} and its a pass")
elif avg < 50:
    print(f"your grade is {avg} and you're fail")
else:
    print("plese enter a valid grade")