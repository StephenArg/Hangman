import random

words = []                                      # establishes variable for word list
with open("words.txt", "r+") as file:           # opens file with words and appends ones 7 letters or longer into words
    for word in file.read().splitlines():
        if len(word) >= 7:
            words.append(word)
random_word = random.choice(words)              # randomly chooses word from word list
word_length = len(random_word)                  # checks word length for later use
random_word_checker = ""                        # string variable for checking word
pre_random_word_checker = []                    # list to store word in letter by letter
random_word_cache = ""                          # cache for random word
word_array = []                                 # list of already made guesses
visual_cache_array = []                         # list to display letters found with _'s in between
wrong_guess_array = []                          # list of wrong letters to prevent second guesses
count = 0
count2 = 0
count3 = 0
count4 = 0
chances_counter = 0
chances = 7


def is_letter_in_word(var):                   # function to determine if the guessed letter is in the word
    for x in word_array:                      # checks letter by letter in list
        if var == x:                         # if the letter matches it prints Nice guess and returns True
            print("Nice guess!\n")
            wrong_guess_array.append(var)    # it also adds the letter to the wrong_guess list so it won't be picked
            return True
        else:
            wrong_guess_array.append(var)     # just sends letter to wrong_guess list, not True


for letter in random_word:                  # turns random word string into list
    word_array.append(letter)

while count < word_length:                  # for the length of the word, sets up string with that many _'s with a space
    random_word_cache += "_ "
    count += 1

for dash in random_word_cache:              # for each character in random_word_cached "_ _ _ _ "...etc it..
    visual_cache_array.append(dash)         # stores them into visual_cache list to be shown later

print("\n","Welcome! Let's play hangman!")
print("\n","This word contains", word_length, "letters.")
print("\n", random_word_cache)

while count2 < 10000:       # was originally set to 35, but 10k seems less likely to be reached by the average player
    if count2 < 1:          # sets initial round up visually
        guess = (input("Pick a letter: "))      # asks user to pick letter
        guess = guess.lower()       # lowers users input case
        if guess in wrong_guess_array:      # not necessary for first round, but w/e. checks for guess to have been
            print("You guessed that already! Try again!\n")     # guessed already
        else:
            if is_letter_in_word(guess):        # if word hasn't been guessed check if letter is in word. If True:
                while count3 < word_length:     # while loop counting through word length
                    if word_array[count3] == guess:   # is guess is in the letter within that list's position
                        visual_cache_array[count3 * 2] = guess  # revalues the visual cache list at the relevant..
                        count3 += 1                       # position to the guessed letter, then furthers the count
                    else:
                        count3 += 1     # other wise furthers the count with no changes. Goes through whole word list
                count2 += 1   # furthers game counter
            else:
                try:
                    int_guess = int(guess)
                    print("Please don't guess numbers.\n")
                except:
                    pass
                if len(guess) > 1:
                    if guess.isalpha() and not guess.isdigit():
                        print("That's too many characters! Only try one letter next time.\n")
                        count2 += 1
                    elif guess.isdigit():
                        count2 += 1
                    else:
                        print("You used to many characters.. and I'm pretty sure some of those aren't even letters.\n")
                        count2 += 1
                elif guess.isalpha():
                    chances_counter += 1        # if guess is not in word, -1 chance,
                    print("Wrong guess. Try again!\n")
                    count2 += 1
                else:
                    print("You used a non-letter character. Please don't do that!\n")
                    count2 += 1
    else:
        if random_word_checker == random_word:  # checks to see if you won
            print(random_word.upper())    # prints word in CAPS
            print("You win! Thanks for playing!")
            break       # stops game
        else:
            random_word_cache = ""  # clears cache. This is used to generate the visual of guessed letters
            print("Guesses remaining: ", (chances - chances_counter))   # displays remaining chances
            for underscore in visual_cache_array:  # inserts visual_cache list one character at a time into string
                random_word_cache += underscore
            print(random_word_cache)    # prints string showing remaining spaces
            if chances_counter >= chances:  # checks to see if you lost
                print(random_word)      # prints lower case version of random word
                print("You lose. Try again next time!")
                break       # ends game
            guess = (input("Pick a letter: "))  # if you didn't win or lose it asks for an input
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
                    try:
                        int_guess = int(guess)
                        print("Please don't guess numbers.\n")
                    except:
                        pass
                    if len(guess) > 1:
                        if guess.isalpha() and not guess.isdigit():
                            print("That's too many characters! Only try one letter next time.\n")
                            count2 += 1
                        elif guess.isdigit():
                            count2 += 1
                        else:
                            print(
                                "You used to many characters.. and I'm pretty sure some of those aren't even letters.\n")
                            count2 += 1
                    elif guess.isalpha():
                        chances_counter += 1  # if guess is not in word, -1 chance,
                        print("Wrong guess. Try again!\n")
                        count2 += 1
                    else:
                        print("You used a non-letter character. Please don't do that!\n")
                        count2 += 1
        count4 = 0
        pre_random_word_checker = []   # clears list
        random_word_checker = ""       # clears string
        while count4 < len(visual_cache_array):
            pre_random_word_checker.append(visual_cache_array[count4])  # makes a list from all even spaces in
            count4 += 2                                         # visual_cache list. Even spaces won't have ""
        for i in pre_random_word_checker:       # goes through pre_checker list and converts it to string
            random_word_checker += i         # compares this variable to the random word each round until it's the same
        count2 += 1
