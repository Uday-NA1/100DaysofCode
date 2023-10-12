# Created hangman game

import random
from day7_art import stages, logo
from day7_words import word_list

game_over = False
word_list = [word_list]
hangman_word = random.choice(word_list)
word_len = len(hangman_word)
lives = 6

print(logo)

display = []
for _ in range(word_len):
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed '{guess}' and it is correct.")
    
    for position in range(word_len):
        letter = hangman_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in hangman_word:
        print(f"You've guessed {guess}, which is incorrect. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True    
            print("You Lose!")
    
    if "_" not in display:
        game_over = True
        print("You Win!")
    
    print(stages[lives])