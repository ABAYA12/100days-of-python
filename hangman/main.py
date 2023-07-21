import random
# import the logo and stages from hangman_art.py
from hangman_art import logo, stages
# import the list of words from hangman_word.py
from hangman_word import word_list
print(logo)
print("Welcome to Hangman Game🙋‍♂️🙋‍♀️\nREMEMBER YOU HAVE 6 LIVES AND YOU LOOSE A LIFE FOR WRONG GUESS")
print()

chosen_word = random.choice(word_list)  # choose a random word from the list
print(f'Pssst, the solution is {chosen_word}.')

dispaly = []  # create an empty list
word_length = len(chosen_word)  # Set the word length to a variable
for _ in range((word_length)):  # loop through the word length
    dispaly += "_"  # Add undescores to display to represent the number of letters in the chosen word
print(dispaly)

lives = 6  # create a variable to store the number of lives of the user
end_of_game = False  # create a variable to check if the game has ended
while not end_of_game:  # loop through the game
    # ask the user to guess a letter
    guess = str(input("Guess a letter: ")).lower()
    if guess in dispaly:  # check if the guess is in the display
        print(f"You have already guessed {guess}.")  # print a message

    for position in range(word_length):  # loop through the word length
        # assign the letter in the chosen word to a variable
        letter = chosen_word[position]
        if letter == guess:       # check if the letter is equal to the guess
            # replace the underscore with the letter
            dispaly[position] = letter
    print(dispaly)

    if guess not in chosen_word:  # check if the guess is not in the chosen word
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1  # reduce the number of lives by 1
        if lives == 0:  # check if the number of lives is 0
            end_of_game = True  # end the game
            print()
            print("You lose!🙆‍♂️🙆‍♀️\n")
            print(f'Pssst, the solution is {chosen_word}.')

    if "_" not in dispaly:  # check if there is no underscore in the display
        end_of_game = True  # end the game
        print()
        print(f"Hey {logo}")
        print("You win💇‍♂️.\n")
        print(f'Pssst, the solution is {chosen_word}.')
