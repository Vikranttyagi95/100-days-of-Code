# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
final_bill = 0

if size == 'S':
    if add_pepperoni == 'Y':
        small_pizza += 2
    final_bill = small_pizza

if size == 'M':
    if add_pepperoni == 'Y':
        medium_pizza += 3
        
    final_bill = medium_pizza

if size == 'L':
    if add_pepperoni == 'Y':
        large_pizza += 3
        
    final_bill = large_pizza

if extra_cheese == 'Y':
    final_bill += 1

print(f"Your final bill is: %{final_bill}")


    
