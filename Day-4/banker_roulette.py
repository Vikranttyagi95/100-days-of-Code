# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_len = len(names)

rand_ind = random.randint(0, names_len-1)
person = names[rand_ind]
print(f"{person} is going to pay the meal today!")
