import random
from hangman_words import word_list
import replit
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_the_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

display = []
for _ in range(word_length):
    display += "_"
print(display)

letters = []
counter = 1
while not end_of_the_game:
    if counter > 1:
        print(f"Used letters: {letters}")
    guess = input("Guess a letter: ").lower()
    replit.clear()
    if guess in display:
        print(f"You've already guessed {guess}")
        

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            counter += 1

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        counter += 1

        if lives == 0:
            end_of_the_game = True
            print("You lose.")
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_the_game = True
        print("You win.")
    print(stages[lives])  
    letters += guess

print(f"You used: {letters}")        
print(f"The word was: {chosen_word}\n")