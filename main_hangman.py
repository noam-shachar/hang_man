def wellcom_to_hangman():
    HANGMAN_ASCII_ART = """ welcome to the game hangman

      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/
     """
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART,
          MAX_TRIES)

def check_valid_input(letter_guessed, old_letters_guessed):
    """ the function returns if the gussed letter is legal (havent been guused and just a letter)
    :param letter_guessed: a letter the player guess
    :param old_letters_guessed: list of the letters that already been guessed
    :type letter_guessed: string
    :type old_letters_guessed: list (of strings)
    return if the letter is legal
    :rtype: bool"""
    if (len(letter_guessed) == 1) and (letter_guessed.isalpha() == True) and old_letters_guessed.count(letter_guessed.lower()) == 0:
        return True
    else:
        return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    """ the function return if the letter is legal and add it to the list of the letter guessed
    or if not legal prints "X" and the list of old guess in lower case
    divided by "->"
    :param letter_guessed_1: the letter the player guess
    :param old_letters_guessed_1: a list of preveius guesses, can be lower or upper case
    :type letter_guessed_1: basestring
    :type old_letters_guessed_1: list (of strings)
    :return: True if legal, if not legal False
    :rtype: bool"""
    if (check_valid_input(letter_guessed, old_letters_guessed) == True):
        #old_letters_guessed = old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        old_letters_guessed_sorted = sorted(old_letters_guessed, key=str.lower)
        old_letters_guessed_sorted_lower = [x.lower() for x in old_letters_guessed_sorted]
        print("X")
        print(" -> ".join(old_letters_guessed_sorted_lower))
        return False

def choose_word(file_path, index):
    file_of_words = open(file_path, "r+")
    string_of_words = file_of_words.read()
    list_of_words = string_of_words.split(" ")
    original_sentence_in_list = string_of_words.split(" ")
    j = 0
    for word2 in original_sentence_in_list:
        if "\n" in word2:
            original_sentence_in_list[j] = word2[:-2]
        j += 1
    for word in list_of_words:
        count = 0
        for word1 in list_of_words:
            if word == word1:
                count += 1
            if count > 1:
                list_of_words.remove(word)
                count -= 1
    the_length = len(list_of_words)
    the_chosen_word = original_sentence_in_list[(index % len(original_sentence_in_list)) - 1]
    file_of_words.close()
    return (the_length, the_chosen_word)

def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {1: """    x-------x"""}
    HANGMAN_PHOTOS[2] = """    x-------x
    |
    |
    |                 
    |
    |"""
    HANGMAN_PHOTOS[3] = """    x-------x
    |       |
    |       0
    |
    |
    |"""

    HANGMAN_PHOTOS[4] = """    x-------x
    |       |
    |       0
    |       |
    |
    |"""

    HANGMAN_PHOTOS[5] = """    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |"""

    HANGMAN_PHOTOS[6] = """    x-------x
    |       |
    |       0
    |      /|\          
    |      /
    |"""

    HANGMAN_PHOTOS[7] = """    x-------x
    |       |
    |       0
    |      /|\  
    |      /|\ 
    |           
        you lose!"""
    print(HANGMAN_PHOTOS[num_of_tries])
    return None

def show_secret_word(secret_word, old_letters_guessed):
    """ the func
    :type secret_word: string
    :type old_letters_guessed: list"""
    unlocked_secret_word = "_ " * len(secret_word)
    list_of_wrong_guesses = []
    for letter in old_letters_guessed:
        count_letter = 0
        i = 0
        for char in secret_word:
            if letter == char:
                unlocked_secret_word = unlocked_secret_word[:i * 2] + char + unlocked_secret_word[(i * 2 + 1):]
                count_letter += 1
            i += 1
        if count_letter == 0:
            list_of_wrong_guesses += [letter]
    return unlocked_secret_word[0:-1]

def len_list_of_wrong(secret_word, old_letters_guessed):
    list_of_wrong_guesses = []
    for letter in old_letters_guessed:
        count_letter = 0
        for char in secret_word:
            if letter == char:
                count_letter += 1
        if count_letter == 0:
            list_of_wrong_guesses += [letter]
    len_list_of_wrong_letters = len(list_of_wrong_guesses)
    return len_list_of_wrong_letters




def main():
    if __name__ == "__main__":
        wellcom_to_hangman()
        file_path = input("enter the file path: ")
        index = int(input("enter the index u want: "))
        print("lets start!")
        secret_word = choose_word(file_path, index)[1]
        old_letters_guessed = []
        print_hangman(1)
        print(show_secret_word(secret_word, old_letters_guessed))
        num_of_tries = 1
        while num_of_tries < 6:
            letter_guessed = input("guess a letter: ")
            letter_guessed.lower()
            if check_valid_input(letter_guessed, old_letters_guessed) == True:
                old_letters_guessed += [letter_guessed.lower()]
                if letter_guessed not in secret_word:
                        num_of_tries = len_list_of_wrong(secret_word, old_letters_guessed)
                        print_hangman(num_of_tries + 1)
                print(show_secret_word(secret_word, old_letters_guessed))
                if list(secret_word) == show_secret_word(secret_word, old_letters_guessed).split(" "):
                    print("you won!")
                    break
            else:
                try_update_letter_guessed(letter_guessed, old_letters_guessed)
main()







        








