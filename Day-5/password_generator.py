#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

final_list = []
for i in range(nr_letters):
    rand_index = random.randint(0,25)
    letter = letters[rand_index]
    final_list.append(letter)

sym_len = len(symbols)
for i in range(nr_symbols):
    rand_index = random.randint(0,sym_len-1)
    sym = symbols[rand_index]
    final_list.append(sym)

for i in range(nr_numbers):
    rand_index = random.randint(0,9)
    num = numbers[rand_index]
    final_list.append(num)

random.shuffle(final_list)

password = "".join(final_list)
print(f"Your password is: {password}")
