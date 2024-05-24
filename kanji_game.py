#!/usr/bin/env python3

import time
import random
import os
import platform
from tqdm import tqdm

file_path = "/Users/coleshanks/Documents/GitHub/kanji_game/words.txt"

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def loading(duration=5):
    for _ in tqdm(range(10), desc="Building", ncols=100):
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

def initialize_game():

    time.sleep(0.2)
    print("The game is being initialized")

    loading()

    words = read_words(file_path)  # Call read_words and store the result in words
    time.sleep(2)
    print("Building words list...")

    # Initialize empty lists for words and readings
    words_list = []
    readings_list = []
    time.sleep(1)
    print("Building arrays...")

    # Simple for loop to iterate over the list of tuples
    for word, reading in words:
        words_list.append(word)  # Append the word to words_list
        readings_list.append(reading)  # Append the reading to readings_list
    time.sleep(0.8)
    print("Reading words/readings into tuples...")

    # Generate a random index
    word_size = len(words_list)
    random_index = get_random_index(word_size)

    # Get random word and reading using the same index
    random_word = get_random_word(words_list, random_index)
    random_reading = get_random_reading(readings_list, random_index)

    time.sleep(3)
    print("Initialization complete...")
    time.sleep(0.3)
    print("Entering game state...\n")

    return word_size, words_list, readings_list  # Return as a tuple

def game(word_size, words_list, readings_list):
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    print("Welcome to the kanji game. Enter 'quit' at any point to return to the main menu\n")
    while True:

        index = get_random_index(word_size)
        word = get_random_word(words_list, index)
        reading = get_random_reading(readings_list, index)

        print(word_size) #for debugging
        print(f"index: {index} #for debugging purposes")
        print(f"{BLUE}{word}{RESET}")
        answer = input("Enter the reading\n")
        if answer == reading:
            print(f"{GREEN}correct!{RESET}\n")
            quit_game =input("Press any key to continue...")
            if quit_game in ['quit', 'q', 'Quit', 'Q']:
                break
            clear()
        elif answer in ['quit', 'q', 'Quit', 'Q']:
            break
        else:
            print(f"incorrect! The correct reading is: {GREEN}{reading}{RESET}")
            quit_game =input("Press any key to continue...")
            if quit_game in ['quit', 'q', 'Quit', 'Q']:
                break
            clear()

def main():
    while True:
        clear()
        print("Welcome to the MAIN MENU\n")
        choice = input("Would you like to play kanji_game? (yes/no)\n").strip().lower()
        if choice in ['yes', 'y']:
            word_size, words_list, readings_list = initialize_game()

            game(word_size, words_list, readings_list)

        elif choice in ['no', 'n']:
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please type 'yes or no'")
    print("Game over...\n")

if __name__ == "__main__":
    main()
