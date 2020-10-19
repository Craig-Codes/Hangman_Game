# Hangman game - User is given a random word from word_list.txt and gets 7 guesses

import random  # random module imported to easily pull out a random entry from a list

# Global Variables
game_word_bank = []  # Global array to store the bank of imported words
guessed_letters = []  # list to store the guessed letters, user input adds a letter into this list
guessed_word = ""  # empty guessed word variable, populated once text file is opened and randomised
guess_counter = 7  # variable used to keep track of user guesses

# import the word_list.txt file and add read each line before appending to the game_world_bank variable
file_path = "word_list.txt"
with open(file_path, "r") as file:
    for line in file:
        # loop through each line in the file, and add it to the list.
        game_word_bank.append(line.strip())

word = random.choice(game_word_bank)  # random.choice method pulls a random entry from the list assigning it to word
word_list = list(word)  # List of the letters from the random word


# Counter function - controls the players guess count
# function takes the user input and checks to see if the letter is in the word_list variable
def guess_number(input_letter):
    global guess_counter
    if input_letter not in word_list:
        guess_counter -= 1  # decrease the counter by 1
        if guess_counter == 0:  # if guessed more than 7 times player loses and game ends
            print("You lose")
            print("The word was {}".format(word))
            exit()


# Known letter function - controls how the player sees the guessed word during the game
# function loops through word_list, checking to see if user input (guessed_letters) matches a list entry.
def letter_guess():
    global guessed_word
    guessed_word = ""
    for entry in word_list:
        if entry in guessed_letters:
            # If a letter matches, the letter is concatenated to the guessed_word variable
            guessed_word += entry
        else:
            # If a letter isn't found, a * is concatenated to the guess_word variable
            guessed_word += "*"


# Completion check function - checks to see if player has won the game
# Player wins if the guesses_word list contains the exact same elements as the guessed_word
def completed_check():
    global guessed_word, word
    if word == guessed_word:
        print("Congratulations you win")
        exit()


letter_guess()  # call letter_guess function at the start to give user the starting word

# Print statements give player information before the game starts
print("***** Welcome to the Hangman Game *****")
print("The game will end when you make 7 incorrect guesses, or you correctly guess the word... good luck! \n")

# While loop keeps running until player loses game or word is guessed
while "*" in guessed_word:
    print("The word you are guessing is {}".format(guessed_word))
    print("You have {} guesses left".format(guess_counter))
    print("You have already guessed these letters: {}".format(guessed_letters))
    letter = str(input("Please enter your next guess: ")).lower()
    guessed_letters.append(letter)
    letter_guess()
    guess_number(letter)
    completed_check()
