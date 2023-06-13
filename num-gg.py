from art import logo
import random


# 'The Machine' enters the number for itself
# # def machine_input(low, high):
# #     number = random.randint(low, high)
# #     return str(number)
# #
# #
# # random_number = machine_input(1, 10)
# # user_input = input("Enter a random number: " + random_number + " ")


EASY_MODE = 10
HARD_MODE = 5


def guessing():
    """Lives Counter: - 1"""
    return difficulty() - 1


def difficulty():
    """User picks a difficulty"""
    valid_input = False
    user_choice_difficulty = input("Type 'easy' for 10 lives, type 'hard' for 5 lives\nChoose a difficulty: ")
    while not valid_input:
        if user_choice_difficulty == "easy":
            return EASY_MODE
        elif user_choice_difficulty == "hard":
            return HARD_MODE
        elif user_choice_difficulty != "easy":
            user_choice_difficulty = input("    Invalid Input.\nType 'easy' for 10 lives, type 'hard' for 5 lives: ")


def number_guessing_game():
    """Just the game, nothing else."""
    game_over = False
    random_number = random.choice(range(1, 101))

    print(logo)
    print(f"                                      This is the secret number: {random_number}\n")  # Cheat Mode

    user_lives = difficulty()
    print(f"    You have {user_lives} lives.")
    user_pick = int(input("Guess the number between 1 and 100: "))

    for lives in range(user_lives):
        while not game_over:
            if random_number == user_pick:
                print(f"    Congratulations! {user_pick} is the right number.\n")
                game_over = True
            elif user_lives == 1:
                print("    You lose.\n")
                print(f"The secret number was: {random_number}\n")
                game_over = True
            elif user_pick > random_number:
                user_lives -= 1
                print("    Too High. Are you high? Ooh you don't wanna find out how high i can fly!")
                print(f"    You have {user_lives} lives left.")
                user_pick = int(input("Guess a lower number: "))
            elif user_pick < random_number:
                user_lives -= 1
                print("    Too Low. Just like your life's standards.")
                print(f"    You have {user_lives} lives left.")
                user_pick = int(input("Guess a higher number: "))


while input("Do you want to play the Number-Guessing-Game? Type 'y' or 'n': ") == "y":
    number_guessing_game()
