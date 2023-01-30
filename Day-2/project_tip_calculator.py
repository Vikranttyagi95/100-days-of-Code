print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? "))

tip_perc = int(input("What percentage tip would you like to give? "))

persons = int(input("How many people to split the bill? "))

bill_with_tip = total_bill * (1 + tip_perc/100)

each_share = round(bill_with_tip / persons, 2)

print(f"Each person should pay ${each_share}")
