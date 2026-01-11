#!/usr/bin/env python3
"""
A simple number guessing game.
The computer picks a random number between 1 and 10, and you try to guess it.
"""

import random


def main():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()