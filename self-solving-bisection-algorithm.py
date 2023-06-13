import random


EASY_MODE = 10
HARD_MODE = 5


def guessing(lives):
    """Lives Counter: - 1"""
    return lives - 1


def difficulty():
    """User picks a difficulty"""
    valid_input = False
    user_choice_difficulty = input(
        "Type 'easy' for 10 lives, type 'hard' for 5 lives\nChoose a difficulty for 'The Machine': ")
    while not valid_input:
        if user_choice_difficulty == "easy":
            return EASY_MODE
        elif user_choice_difficulty == "hard":
            return HARD_MODE
        elif user_choice_difficulty != "easy":
            user_choice_difficulty = input("    Invalid Input.\nType 'easy' for 10 lives, type 'hard' for 5 lives: ")


def bisection_algorithm(target, epsilon, lives):
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
    """Just the game, nothing else."""
    random_number = random.choice(range(1, 101))

    user_lives = difficulty()
    print(f"\n'The Machine' has {user_lives} lives.")

    guess = bisection_algorithm(random_number, 0.01, user_lives)

    if guess == random_number:
        print(f"\nThe correct number is {guess}.")
    else:
        print(f"\nThe correct number is {random_number}.")


while input("Do you want 'The Machine' to play the Number-Guessing-Game? Type 'y' or 'n': ") == "y":
    number_guessing_game()
