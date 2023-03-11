#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for letter in chosen_word]

while "_" in display:
    guess = input("Guess a letter: ").lower()
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    print(display)

print("You won!")

