import random
import string


def load_words(): 
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('words.txt', 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words() # global var to access the wods in the program


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if len(set(secret_word).difference(set(letters_guessed))) == 0:
        return True
    else:
        return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed = ['_ ' for _ in range(len(secret_word))]
    common = list(set(secret_word).intersection(set(letters_guessed)))
    for j in range(len(common)):
        for i in range(len(secret_word)):
            if secret_word[i] == common[j]:
                guessed[i] = common[j]

    return guessed 



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    consonants = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    available = list(set(consonants).difference(set(letters_guessed)))
    return ''.join(sorted(available))
    
    

def hangman(secret_word):
    vowels = list("aeiou")
    guesses_left = 6
    warnings_left = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))
    letters_guessed = []
    while guesses_left > 0:
        print("You have {} guesses left".format(guesses_left))
        print("You have {} warnings left".format(warnings_left))
        print("Available letters:", get_available_letters(letters_guessed))
        char = str(input("Please guess a letter: ")).lower()
        if not (char.isalpha()): #invalid input, if a character is not entered
            if warnings_left == 0:
                guesses_left -= 1
            else:
                warnings_left -= 1
            print("------------------")
            continue

        elif char in letters_guessed: #invalid input, an already guessed char
            print("Error: The letter has already been guessed.") 
            if warnings_left == 0:
                guesses_left -= 1
            else:
                warnings_left -= 1
            print("------------------")
            continue

        else: #valid guess
            letters_guessed.append(char)
            if char not in secret_word: # but guess is wrong
                print("Oops! this letter is not in my word",
                        ''.join(get_guessed_word(secret_word, letters_guessed)))
                if char in vowels:
                    guesses_left -= 2
                else:
                    guesses_left -= 1
                print("------------------")
                continue

            else:
                print("Good Guess:", ''.join(get_guessed_word(secret_word,
                    letters_guessed)))
                print("-------------------")

                if is_word_guessed(secret_word, letters_guessed):
                    print("Congratulations you won: ")
                    total_score = guesses_left*len(set(secret_word))
                    print("Your total score for the game is:", total_score)
                    return
                else:
                    continue

    print("You Lost!\nBetter luck next time")
    print("The word is: {}".format(secret_word))
    choice = input("Wanna play again? y/n: ")
    if choice is 'y' or choice is 'Y':
        play()




def match_with_gaps(my_word, other_word):
    '''
    match the current guessed letters including space with 'other_word'
    '''
    count = 0
    for i in range(len(other_word)):
        if my_word[i] == '_ ' or my_word[i] == other_word[i]:
            count += 1
            continue
        else:
            break

    if count == len(other_word):
        return True
    else:
        return False



def show_possible_matches(my_word):
    """
    show potential matches for the current guesses
    """
    flag = 0
    for i in wordlist:
        if len(my_word) == len(i) and match_with_gaps(my_word, i):
            flag = 1
            print(i)
        else:
            continue

    if flag == 0:
        print("No matches found")
        
def hangman_with_hints(secret_word):
    '''
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    '''
    vowels = list("aeiou")
    guesses_left = 6
    warnings_left = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))
    letters_guessed = []
    while guesses_left > 0:
        print("You have {} guesses left".format(guesses_left))
        print("You have {} warnings left".format(warnings_left))
        print("Available letters:", get_available_letters(letters_guessed))
        char = str(input("Please guess a letter: ")).lower()
        if char == '*': # shows possible matches if available
            if not letters_guessed:
                print("There are no possible matches.\nPlease make a guess first")
            else:
                print("The possible matches are:")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print("-------------------")
            continue

        elif not (char.isalpha()): #invalid input, if a character is not entered
            if warnings_left == 0:
                guesses_left -= 1
            else:
                warnings_left -= 1
            print("------------------")
            continue

        elif char in letters_guessed: #invalid input, an already guessed char
            print("Error: The letter has already been guessed.") 
            if warnings_left == 0:
                guesses_left -= 1
            else:
                warnings_left -= 1
            print("------------------")
            continue

        else: #valid guess
            letters_guessed.append(char)
            if char not in secret_word: # but guess is wrong
                print("Oops! this letter is not in my word",
                        ''.join(get_guessed_word(secret_word, letters_guessed)))
                if char in vowels:
                    guesses_left -= 2
                else:
                    guesses_left -= 1
                print("------------------")
                continue

            else:
                print("Good Guess:", ''.join(get_guessed_word(secret_word,
                    letters_guessed)))
                print("-------------------")

                if is_word_guessed(secret_word, letters_guessed):
                    print("Congratulations you won: ")
                    total_score = guesses_left*len(set(secret_word))
                    print("Your total score for the game is:", total_score)
                    return
                else:
                    continue

    print("You Lost!\nBetter luck next time")
    print("The word is: {}".format(secret_word))
    choice = input("Wanna play again? y/n: ")
    if choice is 'y' or choice is 'Y':
        play()

def play():
    secret_word = choose_word(wordlist)
    print("'E' for an easy game i.e with hints or press any key for a normal game")
    choice = str(input("Make a choice: "))
    if choice is 'E' or choice is 'e':
        hangman_with_hints(secret_word)
    else:
        hangman(secret_word)

if __name__ == "__main__":
    play()
