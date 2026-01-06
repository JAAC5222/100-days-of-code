import art
import random

while True:
    print(art.alt_logo)
    print("""Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.""")

    number = random.randint(1, 100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > number:
            print("Too high! Guess again.")
            lives -= 1
        else:
            print("Too low! Guess again.")
            lives -= 1

    if lives == 0:
        print("You've run out of guesses!")

    if input("Do you want to play again? Type 'y' or 'n': ") == 'y':
        print("\n" * 20)
    else:
        break

