#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = ["_" for letter in chosen_word]

end_of_game = False
lives = len(stages)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    
    if guess not in chosen_word:
        print(stages[lives-1])
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("You lost!")        

    if "_" not in display:
        end_of_game = True
        print("You won!")
    
    print(display)

