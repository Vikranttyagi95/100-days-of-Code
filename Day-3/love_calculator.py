# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_names = name1 + ' ' + name2
both_names = both_names.lower()

t_count = both_names.count('t')
r_count = both_names.count('r')
u_count = both_names.count('u')
e_count = both_names.count('e')

true_count = t_count + r_count + u_count + e_count

l_count = both_names.count('l')
o_count = both_names.count('o')
v_count = both_names.count('v')

love_count = l_count + o_count + v_count + e_count

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40  and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")