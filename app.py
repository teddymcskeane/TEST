#!/usr/bin/env python3
"""
An improved hello script that greets the user, chats a bit, and shows the current date and time.
"""

import datetime
import re


def main():
    # Get the user's name
    user_name = input("What's your name? ")
    # Print a personalized greeting
    print(f"Hello, {user_name}!")
    print(f"Hello {user_name}! I am Jarvis, your friendly chatter.")
    # Ask how they're doing
    response = input(f"How are you doing today {user_name}? ").lower()
    # Check for positive response
    if "good" in response or "fine" in response or "great" in response or "well" in response:
        print("Good, me too!")
        while True:
            print("Is there anything I could do for you today?")
            user_request = input().lower()
            if "no" in user_request or "bye" in user_request:
                print("Okay if you need me just text and I'll be back")
                while True:
                    text = input()
                    if not text:
                        break
                    print("Hello! I'm back. What do you need?")
                    user_request = input().lower()
                    # Process the request again
                    if "joke" in user_request:
                        print("Why don't scientists trust atoms? Because they make up everything!")
                    elif "time" in user_request or "date" in user_request:
                        now = datetime.datetime.now()
                        print(f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")
                    elif "help" in user_request or "advice" in user_request:
                        print("I'm here to help! What specifically do you need advice on?")
                    elif "sing" in user_request or "song" in user_request:
                        print("🎵 Twinkle, twinkle, little star... 🎵")
                    elif "about" in user_request and "you" in user_request:
                        print("I'm Jarvis, an AI assistant created to chat and help!")
                    elif "motivate" in user_request or "motivation" in user_request:
                        print("Believe you can and you're halfway there. - Theodore Roosevelt")
                    elif "fact" in user_request:
                        print("Did you know? Octopuses have three hearts!")
                    elif any(op in user_request for op in ['+', '-', '*', '/', '**', '//', '%']):
                        match = re.search(r'(\d+(?:\s*[\+\-\*\/\%\*\*\/\/]\s*\d+)+)', user_request)
                        if match:
                            expr = match.group(1).replace(' ', '')
                            try:
                                result = eval(expr)
                                print(f"The answer is {result}")
                            except:
                                print("Sorry, I couldn't calculate that.")
                        else:
                            print("Sorry, I couldn't find a math expression.")
                    elif "quote" in user_request:
                        print("The only way to do great work is to love what you do. - Steve Jobs")
                    elif "news" in user_request:
                        print("I don't have real-time news, but remember to stay informed!")
                    elif "story" in user_request:
                        print("Once upon a time, there was a coder who built an amazing chatbot...")
                    elif "compliment" in user_request:
                        print("You're doing great! Keep learning Python!")
                    elif "weather" in user_request:
                        print("In Donegal, Ireland, it's often rainy and windy, but the landscapes are stunning!")
                    else:
                        print("That sounds interesting! Tell me more.")
                    print("Anything else?")
                    more = input().lower()
                    if "no" in more:
                        break
                break
            # process user_request
            if "joke" in user_request:
                print("Why don't scientists trust atoms? Because they make up everything!")
            elif "time" in user_request or "date" in user_request:
                now = datetime.datetime.now()
                print(f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")
            elif "help" in user_request or "advice" in user_request:
                print("I'm here to help! What specifically do you need advice on?")
            elif "sing" in user_request or "song" in user_request:
                print("🎵 Twinkle, twinkle, little star... 🎵")
            elif "about" in user_request and "you" in user_request:
                print("I'm Jarvis, an AI assistant created to chat and help!")
            elif "motivate" in user_request or "motivation" in user_request:
                print("Believe you can and you're halfway there. - Theodore Roosevelt")
            elif "fact" in user_request:
                print("Did you know? Octopuses have three hearts!")
            elif any(op in user_request for op in ['+', '-', '*', '/', '**', '//', '%']):
                match = re.search(r'(\d+(?:\s*[\+\-\*\/\%\*\*\/\/]\s*\d+)+)', user_request)
                if match:
                    expr = match.group(1).replace(' ', '')
                    try:
                        result = eval(expr)
                        print(f"The answer is {result}")
                    except:
                        print("Sorry, I couldn't calculate that.")
                else:
                    print("Sorry, I couldn't find a math expression.")
            elif "quote" in user_request:
                print("The only way to do great work is to love what you do. - Steve Jobs")
            elif "news" in user_request:
                print("I don't have real-time news, but remember to stay informed!")
            elif "story" in user_request:
                print("Once upon a time, there was a coder who built an amazing chatbot...")
            elif "compliment" in user_request:
                print("You're doing great! Keep learning Python!")
            elif "weather" in user_request:
                print("In Donegal, Ireland, it's often rainy and windy, but the landscapes are stunning!")
            else:
                print("That sounds interesting! Tell me more.")
    # Check for negative response
    elif "bad" in response or "terrible" in response or "not good" in response or "sad" in response:
        print("Aw, what's wrong? Is there anything I can do to help?")
        help_response = input().lower()
        if "yes" in help_response:
            need = input("What do you need? ").lower()
            if "joke" in need:
                print("Why don't scientists trust atoms? Because they make up everything!")
            elif "time" in need or "date" in need:
                now = datetime.datetime.now()
                print(f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")
            elif "help" in need or "advice" in need:
                print("I'm here to help! What specifically do you need advice on?")
            elif "sing" in need or "song" in need:
                print("🎵 Twinkle, twinkle, little star... 🎵")
            elif "about" in need and "you" in need:
                print("I'm Jarvis, an AI assistant created to chat and help!")
            elif "motivate" in need or "motivation" in need:
                print("Believe you can and you're halfway there. - Theodore Roosevelt")
            elif "fact" in need:
                print("Did you know? Octopuses have three hearts!")
            elif any(op in need for op in ['+', '-', '*', '/', '**', '//', '%']):
                match = re.search(r'(\d+(?:\s*[\+\-\*\/\%\*\*\/\/]\s*\d+)+)', need)
                if match:
                    expr = match.group(1).replace(' ', '')
                    try:
                        result = eval(expr)
                        print(f"The answer is {result}")
                    except:
                        print("Sorry, I couldn't calculate that.")
                else:
                    print("Sorry, I couldn't find a math expression.")
            elif "quote" in need:
                print("The only way to do great work is to love what you do. - Steve Jobs")
            elif "news" in need:
                print("I don't have real-time news, but remember to stay informed!")
            elif "story" in need:
                print("Once upon a time, there was a coder who built an amazing chatbot...")
            elif "compliment" in need:
                print("You're doing great! Keep learning Python!")
            elif "weather" in need:
                print("In Donegal, Ireland, it's often rainy and windy, but the landscapes are stunning!")
            else:
                print("I'm not sure how to help with that, but I'm learning!")
    else:
        print("Okay, is there anything I can do to help?")
        help_response = input().lower()
        if "yes" in help_response:
            need = input("What do you need? ").lower()
            if "joke" in need:
                print("Why don't scientists trust atoms? Because they make up everything!")
            elif "time" in need or "date" in need:
                now = datetime.datetime.now()
                print(f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")
            elif "help" in need or "advice" in need:
                print("I'm here to help! What specifically do you need advice on?")
            elif "sing" in need or "song" in need:
                print("🎵 Twinkle, twinkle, little star... 🎵")
            elif "about" in need and "you" in need:
                print("I'm Jarvis, an AI assistant created to chat and help!")
            elif "motivate" in need or "motivation" in need:
                print("Believe you can and you're halfway there. - Theodore Roosevelt")
            elif "fact" in need:
                print("Did you know? Octopuses have three hearts!")
            elif any(op in need for op in ['+', '-', '*', '/', '**', '//', '%']):
                match = re.search(r'(\d+(?:\s*[\+\-\*\/\%\*\*\/\/]\s*\d+)+)', need)
                if match:
                    expr = match.group(1).replace(' ', '')
                    try:
                        result = eval(expr)
                        print(f"The answer is {result}")
                    except:
                        print("Sorry, I couldn't calculate that.")
                else:
                    print("Sorry, I couldn't find a math expression.")
            elif "quote" in need:
                print("The only way to do great work is to love what you do. - Steve Jobs")
            elif "news" in need:
                print("I don't have real-time news, but remember to stay informed!")
            elif "story" in need:
                print("Once upon a time, there was a coder who built an amazing chatbot...")
            elif "compliment" in need:
                print("You're doing great! Keep learning Python!")
            elif "weather" in need:
                print("In Donegal, Ireland, it's often rainy and windy, but the landscapes are stunning!")
            else:
                print("I'm not sure how to help with that, but I'm learning!")

  

if __name__ == "__main__":
    main()
