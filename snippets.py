# import random


# Steady Approach Algorithm
# Find a close approximation of the cubed number
# cube = 27
# epsilon = 0.01
# num_guesses = 0
# low = 0
# high = 100
# guess = (high + low) / 2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low) / 2.0
#     num_guesses += 1
# print("num_guesses = ", num_guesses)
# print(guess, "is close to the cube root of", cube)


# Bisection Algorithm
# Find the number between 1 and 100
# target = 51
# epsilon = 0.01
# num_guesses = 0
# low = 1
# high = 100
# guess = (high + low) // 2
#
# while abs(guess - target) >= epsilon:
#     if guess < target:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low) // 2
#     num_guesses += 1
#     print("Guess", num_guesses, ":", guess)
#
# print("num_guesses =", num_guesses)
# print(guess, "is the target number")


# 'The Machine' enters the number for itself
# # def machine_input(low, high):
# #     number = random.randint(low, high)
# #     return str(number)
# #
# #
# # random_number = machine_input(1, 10)
# # user_input = input("Enter a random number: " + random_number + " ")
