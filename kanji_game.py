#!/usr/bin/env python3

file_path = "/Users/coleshanks/Documents/GitHub/kanji_game/words.txt"

def read_words(file):
    words = [] #initiliaze an empty array
    f = open(file, 'r', encoding='utf-8')  # Opens the file and reads it into f with a utf-8 encoding
    for line in f:  # For loop for f (file)
        word, reading = line.strip().split(',')  # Strip whitespace and split each line into word/reading
        words.append((word, reading))  # Add tuple to the words array
    f.close()  # Close the file
    return words

def main():
    words = read_words(file_path)  # Call read_words and store the result in words

    # Initialize empty lists for words and readings
    words_list = []
    readings_list = []

    # Simple for loop to iterate over the list of tuples
    for word, reading in words:
        words_list.append(word)  # Append the word to words_list
        readings_list.append(reading)  # Append the reading to readings_list

    # For demonstration purposes, print the lists
    print("Words:", words_list[5])
    print("Readings:", readings_list[5])

if __name__ == "__main__":
    main()