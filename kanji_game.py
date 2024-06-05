#!/usr/bin/env python3

#import requests
import time
import random
import os
import platform
from tqdm import tqdm

# Global variables

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

# Path to files
default = "/Users/coleshanks/Documents/GitHub/kanji_game/words.txt"
harder_difficulty = "/Users/coleshanks/Documents/GitHub/kanji_game/harder_difficulty.txt"
very_hard = "/Users/coleshanks/Documents/GitHub/kanji_game/very_hard.txt"

# JLPT levels
n5 = "/Users/coleshanks/Documents/GitHub/kanji_game/jisho/n5.txt"
n4 = "/Users/coleshanks/Documents/GitHub/kanji_game/jisho/n4.txt"
n3 = "/Users/coleshanks/Documents/GitHub/kanji_game/jisho/n3.txt"
n2 = "/Users/coleshanks/Documents/GitHub/kanji_game/jisho/n2.txt"
n1 = "/Users/coleshanks/Documents/GitHub/kanji_game/jisho/n1.txt"

# JLPT levels
impossible = "/Users/coleshanks/Documents/GitHub/kanji_game/jisho/arc.txt"

# quote files below
eld = "/Users/coleshanks/Documents/GitHub/kanji_game/quotes.txt"

def colour_test():
    print(f"\n{BLACK}BLACK Text{RESET}\n{RED}RED Text{RESET}\n{GREEN}GREEN Text{RESET}\n{YELLOW}YELLOW Text{RESET}\n{BLUE}BLUE Text{RESET}\n{MAGENTA}MAGENTA Text{RESET}\n{CYAN}CYAN Text{RESET}\n{WHITE}WHITE Text{RESET}\n{BRIGHT_BLACK}BRIGHT_BLACK Text{RESET}\n{BRIGHT_RED}BRIGHT_RED Text{RESET}\n{BRIGHT_GREEN}BRIGHT_GREEN Text{RESET}\n{BRIGHT_YELLOW}BRIGHT_YELLOW Text{RESET}\n{BRIGHT_BLUE}BRIGHT_BLUE Text{RESET}\n{BRIGHT_MAGENTA}BRIGHT_MAGENTA Text{RESET}\n{BRIGHT_CYAN}BRIGHT_CYAN Text{RESET}\n{BRIGHT_WHITE}BRIGHT_WHITE Text{RESET}")

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def loading(duration=5, bar_color=GREEN, text_color=MAGENTA):
    for _ in tqdm(range(10), desc=f"{text_color}Building{RESET}", ncols=100, bar_format=f"{text_color}{{desc}}: {{percentage:3.0f}}%|{bar_color}{{bar}}{RESET}| {{n}}/{{total}}"):
        time.sleep(duration / 100)

# Generate title screen
def title_screen():
    print(f"{BRIGHT_GREEN}  _  __    _      _   _     _   ___  {RESET}")
    print(f"{BRIGHT_GREEN} | |/ /   / \\    | \\ | |   (_) |_ _| {RESET}")
    print(f"{BRIGHT_GREEN} | ' /   / _ \\   |  \\| |   | |  | |  {RESET}")
    print(f"{BRIGHT_GREEN} | . \\  / ___ \\  | . ` |  _| |  | |  {RESET}")
    print(f"{BRIGHT_GREEN} |_|\\_\\/_/   \\_\\ |_| \\_| |___| |___| {RESET}\n\n")
    print(f"{BRIGHT_BLUE}Welcome to the MAIN MENU{RESET}\n")

def read_words(file):
    words = []  # Initialize an empty array
    with open(file, 'r', encoding='utf-8') as f:  # Opens the file and reads it into f with a utf-8 encoding
        for line in f:  # For loop for f (file)
            parts = line.strip().split(',')
            word, reading = parts[0], parts[1]
            definition = ','.join(parts[2:])
            words.append((word, reading, definition))  # Add tuple to the words array
    return words

def read_quotes(quote_file):
    quotes = []  # Empty list

    with open(quote_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        stripped_line = line.strip()
        # Split on the last comma
        last_comma_index = stripped_line.rfind(',')
        quote = stripped_line[:last_comma_index]
        character = stripped_line[last_comma_index + 1:]
        quotes.append((quote, character.strip()))

    # Initialize empty lists for words and readings
    quotes_list = []
    character_list = []

    # Simple for loop to iterate over the list of tuples
    for quote, character in quotes:
        quotes_list.append(quote)  # Append the quote to quotes_list
        character_list.append(character)  # Append the character to character_list

    return quotes_list, character_list

def get_random_index(size):
    return random.randint(0, size - 1)  # Generate a random index between 0 and size-1

def get_random_word(words_list, index):
    return words_list[index]  # Return the word at the given index

def get_random_reading(readings_list, index):
    return readings_list[index]  # Return the reading at the given index

def get_random_definition(definitions_list, index):
    return definitions_list[index]  # Return the definition at the given index

def loading_intro_screen():
    time.sleep(0.2)
    print("The game is being initialized")

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
    print("Game levels:\neasy\nhard\nvery_hard\nn5\nn4\nn3\nn2\nn1\nimpossible")

    difficulty_level = input("\nPlease choose a difficulty\n") # logic for invalid input still needed
    if difficulty_level in ['easy']:
        words = read_words(default)  # Call read_words and store the result in words
    elif difficulty_level in ['hard']:
        words = read_words(harder_difficulty)  # Call read_words and store the result in words
    elif difficulty_level in ['very_hard']:
        words = read_words(very_hard)  # Call read_words and store the result in words
    elif difficulty_level in ['n5']:
        words = read_words(n5)  # Call read_words and store the result in words
    elif difficulty_level in ['n4']:
        words = read_words(n4)  # Call read_words and store the result in words
    elif difficulty_level in ['n3']:
        words = read_words(n3)  # Call read_words and store the result in words
    elif difficulty_level in ['n2']:
        words = read_words(n2)  # Call read_words and store the result in words
    elif difficulty_level in ['n1']:
        words = read_words(n1)  # Call read_words and store the result in words
    elif difficulty_level in ['impossible']:
        words = read_words(impossible)  # Call read_words and store the result in words
    else:
        print("Invalid input. Please try again")

    # Initialize empty lists for words, readings, and definitions
    words_list = []
    readings_list = []
    definitions_list = []

    # Simple for loop to iterate over the list of tuples
    for word, reading, definition in words:
        words_list.append(word)  # Append the word to words_list
        readings_list.append(reading)  # Append the reading to readings_list
        definitions_list.append(definition)  # Append the definition to definitions_list

    # Generate a random index
    word_size = len(words_list)
    random_index = get_random_index(word_size)

    # Get random word, reading, and definition using the same index
    random_word = get_random_word(words_list, random_index)
    random_reading = get_random_reading(readings_list, random_index)
    random_definition = get_random_definition(definitions_list, random_index)

   # loading_intro_screen()

    return word_size, words_list, readings_list, definitions_list  # Return as a tuple

def game(word_size, words_list, readings_list, definitions_list):
    clear()

    quote_list, character_list = read_quotes(eld)

    score = 0
    count = 0

    print("Welcome to the kanji game. Enter 'quit' at any point to return to the main menu\n")
    while True:
        if score in [10, 20, 30, 40, 50]:
            print("Good work!! Keep it up\n\n")

        count = count + 1

        index = get_random_index(word_size)
        word = get_random_word(words_list, index)
        reading = get_random_reading(readings_list, index)
        definition = get_random_definition(definitions_list, index)

        index = get_random_index(len(quote_list))
        quote = get_random_word(quote_list, index)
        character = get_random_reading(character_list, index)

        print(word_size) # for debugging
        print(f"index: {index} #for debugging purposes")
        print(f"{BRIGHT_CYAN}{word}{RESET}")
        answer = input("Enter the reading\n")
        if answer == reading:
            score = score + 1
            print(f"{BRIGHT_GREEN}correct!{RESET}")
            print(f"{BRIGHT_CYAN}{word}{RESET} ({definition})\n")
            print(f"Score: {score}/{count}\n")
            print(f"{quote}")
            print(f"- {character}\n")
            quit_game = input("Press any key to continue or enter 'q' to quit...\n")
            if quit_game in ['quit', 'q', 'Quit', 'Q']:
                print(f"Congratulations! Your score was: {score}/{count}\n")
                input("Press any key to return to the main menu...\n")
                break
            clear()
        elif answer in ['quit', 'q', 'Quit', 'Q']:
            print(f"Congratulations! Your score was: {score}/{count}\n")
            print(f"{quote}")
            print(f"- {character}\n")
            input("Press any key to return to the main menu...\n")
            break
        else:
            print(f"{BRIGHT_RED}incorrect!{RESET} The correct reading is: {reading}")
            print(f"{BRIGHT_CYAN}{word}{RESET} ({definition})\n")
            print(f"Score: {score}/{count}\n")
            print(f"{quote}")
            print(f"- {character}\n")
            quit_game = input("Press any key to continue or enter 'q' to quit...\n")
            if quit_game in ['quit', 'q', 'Quit', 'Q']:
                print(f"Congratulations! Your score was: {score}/{count}\n")
                input("Press any key to return to the main menu...\n")
                break
            clear()

def main():
    while True:
        clear()
        title_screen()
        choice = input(f"{BRIGHT_RED}Would you like to play kanji_game? (yes/no){RESET}\n").strip().lower()
        if choice in ['yes', 'y']:
            word_size, words_list, readings_list, definitions_list = initialize_game()
            game(word_size, words_list, readings_list, definitions_list)
        elif choice in ['no', 'n', 'q']:
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please type 'yes or no'")
            input("Press any key to continue...")
    print("Game over...\n")

if __name__ == "__main__":
    main()
