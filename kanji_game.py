#!/usr/bin/env python3

import random

file_path = "/Users/coleshanks/Documents/GitHub/kanji_game/words.txt"

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
    words = read_words(file_path)  # Call read_words and store the result in words

    # Initialize empty lists for words and readings
    words_list = []
    readings_list = []

    # Simple for loop to iterate over the list of tuples
    for word, reading in words:
        words_list.append(word)  # Append the word to words_list
        readings_list.append(reading)  # Append the reading to readings_list

    # Generate a random index
    word_size = len(words_list)
    print(word_size) #for debugging
    random_index = get_random_index(word_size)

    # Get random word and reading using the same index
    random_word = get_random_word(words_list, random_index)
    random_reading = get_random_reading(readings_list, random_index)

    return word_size, words_list, readings_list  # Return as a tuple

def game(word_size, words_list, readings_list):

    print("Welcome to the kanji game. Enter 'quit' at any point to return to the main menu\n")
    while True:
        print("hello")

        index = get_random_index(word_size)
        word = get_random_word(words_list, index)
        reading = get_random_reading(readings_list, index)


        
        word, reading = initialize_game()
        print(word)
        answer = input("Enter the reading\n")
        if answer == reading:
            print("correct!\n")
            input("Press any key to continue...")
        elif answer in ['quit', 'q', 'Quit', 'Q']:
            break
        else:
            print("incorrect! The correct reading is: ", reading)
            input("\nPress any key to continue...")


def main():
    while True:
        choice = input("Would you like to play kanji_game? (yes/no)\n").strip().lower()
        if choice in ['yes', 'y']:
            print("The game is being initialized")
            input("\nPress any key to continue...\n")
            word_size, words_list, readings_list = initialize_game()

            # For demonstration purposes, print the random word and reading
            #print("Random Word:", random_word)
            #print("Random Reading:", random_reading)

            game(word_size, words_list, readings_list)

        elif choice in ['no', 'n']:
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please type 'yes or no'")
    print("Game over, thanks for playing\n")

if __name__ == "__main__":
    main()
