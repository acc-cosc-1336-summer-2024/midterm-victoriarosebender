#write functions here, don't add input('') statements here!
import random

def game_game():
    choice = 'y'
    while choice == 'y' or choice == "Y":
        
        guess = int(input("Guess a number 1 through 5: "))
        
        guess_game(guess)

        choice = input("Type Y to guess again. Type N to exit.") 

def get_random_number():
    num = random.randint(1,5)
    return num

def guess_game(num):
    test = int(get_random_number())
    if num == test:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry. The number was {test}. Try again.")

