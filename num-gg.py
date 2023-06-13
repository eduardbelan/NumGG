from art import logo
import random
import sys
import os


EASY_MODE = 10
HARD_MODE = 5


def difficulty():
    """
    User picks a difficulty
    """
    valid_input = False
    user_choice_difficulty = input("\nType 'easy' for 10 lives, type 'hard' for 5 lives\nChoose a difficulty: ")
    while not valid_input:
        if user_choice_difficulty == "easy":
            return EASY_MODE
        elif user_choice_difficulty == "hard":
            return HARD_MODE
        elif user_choice_difficulty != "easy":
            user_choice_difficulty = input("    \nInvalid Input.\nType 'easy' for 10 lives, type 'hard' for 5 lives: ")


def number_guessing_game():
    """
    Just the game, nothing else.
    """
    clear = lambda: os.system("cls")
    clear()

    random_number = random.choice(range(1, 101))

    print(logo)
    print(f"                                      This is the secret number: {random_number}\n")  # Cheat Mode

    user_lives = difficulty()
    print(f"    \nYou have {user_lives} lives.")
    user_pick = int(input("Guess the number between 1 and 100: "))

    game_over = False

    for lives in range(user_lives):
        while not game_over:
            if random_number == user_pick:
                print(f"    \nCongratulations! {user_pick} is the right number.")
                game_over = True
            elif user_lives == 1:
                print("    \nYou lose.\n")
                print(f"The secret number was: {random_number}\n")
                game_over = True
            elif user_pick > random_number:
                user_lives -= 1
                print("    \nToo High. Are you high? Ooh you don't wanna find out how high i can fly!")
                print(f"    You have {user_lives} lives left.")
                user_pick = int(input("Guess a lower number: "))
            elif user_pick < random_number:
                user_lives -= 1
                print("    \nToo Low. Just like your life's standards.")
                print(f"    You have {user_lives} lives left.")
                user_pick = int(input("Guess a higher number: "))


def go_again():
    """
    Ask the User to play again
    """
    valid_input = False

    while not valid_input:
        another_one = input("\nDo you want to play the Number-Guessing-Game? (y/n): ")

        if another_one not in ["y", "n"]:
            print("\nInvalid Input.\n ")
        elif another_one == "n":
            clear = lambda: os.system("cls")
            clear()
            sys.exit()
        else:
            number_guessing_game()


go_again()
