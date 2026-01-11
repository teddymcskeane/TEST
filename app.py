#!/usr/bin/env python3
"""
A simple greeting program that welcomes the user and shows the current date.
"""

import datetime


def main():
    # Get the user's name
    name = input("What's your name? ")
    # Print a personalized greeting
    print(f"Hello, {name}!")
    # Show the current date
    today = datetime.date.today()
    print(f"Today's date is {today}.")


if __name__ == "__main__":
    main()
