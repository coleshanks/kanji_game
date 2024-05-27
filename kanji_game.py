#!/usr/bin/env python3

import time
import random
import os
import platform
from tqdm import tqdm

#Global variables
# refer the table for colour code:
# Text Color  Foreground Code
# ANSI color codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Reset color
RESET = "\033[0m"



default = "/Users/coleshanks/Documents/GitHub/kanji_game/words.txt"
harder_difficulty = "/Users/coleshanks/Documents/GitHub/kanji_game/harder_difficulty.txt"

def colour_test():
    print(f"\n{BLACK}Black Text{RESET}")
    print(f"\n{RED}RED Text{RESET}")
    print(f"\n{GREEN}GREEN Text{RESET}")
    print(f"\n{YELLOW}YELLOW Text{RESET}")
    print(f"\n{BLUE}BLUE Text{RESET}")
    print(f"\n{MAGENTA}MAGENTA Text{RESET}")
    print(f"\n{CYAN}CYAN Text{RESET}")
    print(f"\n{WHITE}WHITE Text{RESET}")
    print(f"\n{BRIGHT_BLACK}BRIGHT_BLACK Text{RESET}")
    print(f"\n{BRIGHT_RED}BRIGHT_RED Text{RESET}")
    print(f"\n{BRIGHT_GREEN}BRIGHT_GREEN Text{RESET}")
    print(f"\n{BRIGHT_YELLOW}BRIGHT_YELLOW Text{RESET}")
    print(f"\n{BRIGHT_BLUE}BRIGHT_BLUE Text{RESET}")
    print(f"\n{BRIGHT_MAGENTA}BRIGHT_MAGENTA Text{RESET}")
    print(f"\n{BRIGHT_CYAN}BRIGHT_CYAN Text{RESET}")
    print(f"\n{BRIGHT_WHITE}BRIGHT_WHITE Text{RESET}")


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# def loading(duration=5):
#     for _ in tqdm(range(10), desc="Building", ncols=100):
#         time.sleep(duration / 100)

def loading(duration=5, bar_color=GREEN, text_color=MAGENTA):
    for _ in tqdm(range(10), desc=f"{text_color}Building{RESET}", ncols=100, bar_format=f"{text_color}{{desc}}: {{percentage:3.0f}}%|{bar_color}{{bar}}{RESET}| {{n}}/{{total}}"):
        time.sleep(duration / 100)

def read_words(file):
    words = []  # Initialize an empty array
    with open(file, 'r', encoding='utf-8') as f:  # Opens the file and reads it into f with a utf-8 encoding
        for line in f:  # For loop for f (file)
            word, reading = line.strip().split(',')  # Strip whitespace and split each line into word/reading
            words.append((word, reading))  # Add tuple to the words array
    return words

def get_random_index(size):
    return random.randint(0, size - 1)  # Generate a random index between 0 and size-1

def get_random_word(words_list, index):
    return words_list[index]  # Return the word at the given index

def get_random_reading(readings_list, index):
    return readings_list[index]  # Return the reading at the given index

def loading_intro_screen():
    time.sleep(0.2)
    print("The game is being initialized")

    # loading()

    # Example usage
    loading(bar_color=BRIGHT_CYAN, text_color=BRIGHT_MAGENTA)  # You can change the color as needed

    time.sleep(2)
    print("Building words list...")

    time.sleep(1)
    print("Building arrays...")

    time.sleep(0.8)
    print("Reading words/readings into tuples...")

    time.sleep(3)
    print("Initialization complete...")

    time.sleep(0.3)
    print("Entering game state...\n")
    

def initialize_game():

    difficulty_level = input("Enter easy or hard\n") #logic for invalid input still needed
    if difficulty_level in ['easy']:
            words = read_words(default)  # Call read_words and store the result in words
    elif difficulty_level in ['hard']:
            words = read_words(harder_difficulty)  # Call read_words and store the result in words

    #words = read_words(default)  # Call read_words and store the result in words

    # Initialize empty lists for words and readings
    words_list = []
    readings_list = []

    # Simple for loop to iterate over the list of tuples
    for word, reading in words:
        words_list.append(word)  # Append the word to words_list
        readings_list.append(reading)  # Append the reading to readings_list

    # Generate a random index
    word_size = len(words_list)
    random_index = get_random_index(word_size)

    # Get random word and reading using the same index
    random_word = get_random_word(words_list, random_index)
    random_reading = get_random_reading(readings_list, random_index)

    loading_intro_screen()


    return word_size, words_list, readings_list  # Return as a tuple

def game(word_size, words_list, readings_list):
    clear()

    score = 0
    count = 0

    print("Welcome to the kanji game. Enter 'quit' at any point to return to the main menu\n")
    #colour_test()
    while True:

        count = count + 1


        index = get_random_index(word_size)
        word = get_random_word(words_list, index)
        reading = get_random_reading(readings_list, index)

        print(word_size) #for debugging
        print(f"index: {index} #for debugging purposes")
        print(f"{BRIGHT_CYAN}{word}{RESET}")
        answer = input("Enter the reading\n")
        if answer == reading:
            score = score + 1
            print(f"{BRIGHT_GREEN}correct!{RESET}\n")
            print(f"Score: {score}/{count}")
            quit_game =input("Press any key to continue or enter 'q' to quit...\n")
            if quit_game in ['quit', 'q', 'Quit', 'Q']:
                clear()
                break
            clear()
        elif answer in ['quit', 'q', 'Quit', 'Q']:
            break
        else:
            print(f"{BRIGHT_RED}incorrect!{RESET} The correct reading is: ", reading)
            print(f"Score: {score}/{count}")
            quit_game =input("Press any key to continue or enter 'q' to quit...\n")
            if quit_game in ['quit', 'q', 'Quit', 'Q']:
                clear()
                break
            clear()

def main():
    clear()
    while True:
        print("Welcome to the MAIN MENU\n")
        choice = input("Would you like to play kanji_game? (yes/no)\n").strip().lower()
        if choice in ['yes', 'y']:
            word_size, words_list, readings_list = initialize_game()

            game(word_size, words_list, readings_list)

        elif choice in ['no', 'n', 'q']:
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please type 'yes or no'")
    print("Game over...\n")

if __name__ == "__main__":
    main()
