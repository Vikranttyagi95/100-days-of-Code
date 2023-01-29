# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
curr_age = int(age)

remaining_age = 90 - curr_age

days = remaining_age * 365
weeks = remaining_age * 52
months = remaining_age * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

