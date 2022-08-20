import random
from words import words


def play():
    lives = 6
    random_word = str(random.choice(words))
    letters_in_random_word = 0
    for letter in random_word:
        letters_in_random_word += 1
    already_guessed_list = []
    for letter in random_word:
        print("_", end='')
    while lives > 0 and letters_in_random_word > 0:
        print("\nYou have", lives, "lives left. Use them wisely")
        # more letters to be guessed
        get_guess = input("\nGuess a letter here: ")
        if get_guess in already_guessed_list:
            print("\nYou already guessed this letter. Please guess a different letter.")
        else:
            already_guessed_list.append(get_guess)
            for letter in get_guess:
                if letter in random_word and lives > 0:
                    letters_in_random_word -= 1 * random_word.count(letter)
                    print("\nThat letter is in this word.")
                if get_guess not in random_word and lives > 0:
                    lives -=1
                    print("\nThat letter is not in this word.")
            for letter in random_word:
                if letter in already_guessed_list:
                    print(letter, end = '')
                else:
                    print("_", end = '')
            if lives == 0:
                print("\nOut of lives. The word was", random_word)
                wants_to_play_again = input("Do you want to play again?\n (a) yes\n (b) no: ")
                if wants_to_play_again == "a":
                    play()
            if letters_in_random_word == 0:
                print("\nYou guessed the word correctly.")
                wants_to_play_again = input("Do you want to play again?\n (a) yes\n (b) no: ")
                if wants_to_play_again == "a":
                    play()

play()