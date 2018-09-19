import os
import random

os.chdir("/Users/BasicallySteve/Desktop")
words = []
with open("words.txt", "r+") as file:
    for word in file.read().splitlines():
        if len(word) >= 7:
            words.append(word)
random_word = random.choice(words)
word_length = len(random_word)
random_word_checker = ""
pre_random_word_checker = []
random_word_cache = ""
word_array = []
visual_cache_array = []
wrong_guess_array = []
count = 0
count2 = 0
count3 = 0
count4 = 0
chances_counter = 0
chances = 7


def is_letter_in_word(input):
    for x in word_array:
        if input == x:
            print("Nice guess!\n")
            wrong_guess_array.append(input)
            return True
        else:
            wrong_guess_array.append(input)



for letter in random_word:
    word_array.append(letter)

while count < word_length:
    random_word_cache += "_ "
    count +=1

for dash in random_word_cache:
    visual_cache_array.append(dash)

print("\n","Welcome! Let's play hangman!")
print("\n","This word contains", word_length, "letters.")
print("\n", random_word_cache)

while count2 < 35:
    if count2 < 1:
        guess = (input("Pick a letter: "))
        guess = guess.lower()
        if guess in wrong_guess_array:
            print("You guessed that already! Try again!\n")
        else:
            if is_letter_in_word(guess):
                while count3 < word_length:
                    if word_array[count3] == guess:
                        visual_cache_array[count3 * 2] = guess
                        count3 += 1
                    else:
                        count3 += 1
                count2 +=1
            else:
                chances_counter += 1
                print("Wrong guess. Try again!\n")
    else:
        if random_word_checker == random_word:
            print("Guesses remaining: ", (chances - chances_counter))
            for underscore in visual_cache_array:
                random_word_cache += underscore
            print("\n", random_word.upper())
            print("\n", "You win! Thanks for playing!")
            break
        else:
            random_word_cache = ""
            print("Guesses remaining: ", (chances - chances_counter))
            for underscore in visual_cache_array:
                random_word_cache += underscore
            print(random_word_cache)
            if chances_counter >= chances:
                print(random_word)
                print("You lose. Try again next time!")
            guess = (input("Pick a letter: "))
            guess = guess.lower()
            if guess in wrong_guess_array:
                print("You guessed that already! Try again!\n")
            else:
                if is_letter_in_word(guess):
                    count3 = 0
                    while count3 < word_length:
                        if word_array[count3] == guess:
                            visual_cache_array[count3 * 2] = guess
                            count3 += 1
                        else:
                            count3 += 1
                else:
                    chances_counter += 1
                    print("Wrong guess. Try another letter!\n")
        count4 = 0
        pre_random_word_checker = []
        random_word_checker = ""
        while count4 < len(visual_cache_array):
            pre_random_word_checker.append(visual_cache_array[count4])
            count4 += 2
        for i in pre_random_word_checker:
            random_word_checker += i
        count2 += 1

