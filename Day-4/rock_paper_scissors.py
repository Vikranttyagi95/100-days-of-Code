rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_input = input("Please enter your choice: ").lower()

choice_list = [rock, paper, scissors]

rand_ind = random.randint(0, len(choice_list)-1)

machine_choice = choice_list[rand_ind]

if user_input not in ['rock','paper','scissors']:
    print("You gave an invalid input. Please provide a valid one.")

elif user_input == 'rock' and machine_choice == scissors:
    print(f"Your choice: {rock}")
    print(f"Machine choice: {scissors}")
    print("You win!")

elif user_input == 'rock' and machine_choice == paper:
    print(f"Your choice: {rock}")
    print(f"Machine choice: {paper}")
    print("You lose!")

elif user_input == 'paper' and machine_choice == scissors:
    print(f"Your choice: {paper}")
    print(f"Machine choice: {scissors}")
    print("You lose!")

elif user_input == 'paper' and machine_choice == rock:
    print(f"Your choice: {paper}")
    print(f"Machine choice: {rock}")
    print("You win!")

elif user_input == 'scissors' and machine_choice == rock:
    print(f"Your choice: {scissors}")
    print(f"Machine choice: {rock}")
    print("You lose!")

elif user_input == 'scissors' and machine_choice == paper:
    print(f"Your choice: {scissors}")
    print(f"Machine choice: {paper}")
    print("You win!")

else:
    print("Its a draw!")