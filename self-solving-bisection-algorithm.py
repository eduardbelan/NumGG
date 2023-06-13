import random
import sys
import os
from machine_art import logo

EASY_MODE = 10
HARD_MODE = 5


def guessing(lives):
    """
    Lives Counter: - 1"
    """
    return lives - 1


def difficulty():
    """
    User picks a difficulty
    """
    valid_input = False

    user_choice_difficulty = input(
        "\nType 'easy' for 10 lives, type 'hard' for 5 lives\nChoose a difficulty for 'The Machine': ")

    while not valid_input:
        if user_choice_difficulty == "easy":
            return EASY_MODE
        elif user_choice_difficulty == "hard":
            return HARD_MODE
        elif user_choice_difficulty != "easy":
            user_choice_difficulty = input("    Invalid Input.\nType 'easy' for 10 lives, type 'hard' for 5 lives: ")


def bisection_algorithm(target, epsilon, lives):
    """
    Bisection Algorithm for the Machine to solve the Game
    """
    num_guesses = 0
    low = 1
    high = 100
    guess = (high + low) // 2

    while abs(guess - target) >= epsilon:
        if guess < target:
            print(f"'The Machine' guessed: {guess}. Too low.")
            low = guess
        else:
            print(f"'The Machine' guessed: {guess}. Too high.")
            high = guess
        guess = (high + low) // 2
        num_guesses += 1
        lives = guessing(lives)

        if lives == 0:
            print("'The Machine' loses.")
            break

    if lives != 0:
        print(f"'The Machine' guessed: {guess}. 'The Machine' congratulates itself, correct number!")
    return guess


def number_guessing_game():
    """
    Just the game, nothing else
    """
    clear = lambda: os.system("cls")
    clear()

    random_number = random.choice(range(1, 101))

    print(logo)
    print(f"                                      This is the secret number: {random_number}\n")

    user_lives = difficulty()
    print(f"\n'The Machine' has {user_lives} lives.")

    guess = bisection_algorithm(random_number, 0.01, user_lives)

    if guess == random_number:
        print(f"\nThe correct number is {guess}.")
    else:
        print(f"\nThe correct number is {random_number}.")

    go_again()


def go_again():
    """
    Ask the User to play again
    """
    valid_input = False

    while not valid_input:
        another_one = input("\nDo you want 'The Machine' to play the Number-Guessing-Game? (y/n): ")

        if another_one not in ["y", "n"]:
            print("\nInvalid Input.\n ")
        elif another_one == "n":
            clear = lambda: os.system("cls")
            clear()
            sys.exit()
        else:
            number_guessing_game()


go_again()
