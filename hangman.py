import random
import sys
from english_words import english_words_lower_alpha_set

DIFWORD = False
HANGMAN = False
AGAIN = True
illegal_guess = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", "!",
                "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-",
                "=", ",", ".", "/", "<", ">", "?", ";", ":", "{", "}", "|",
                "\\", "+"]


def ascii_hangman():
    if WRONG_GUESSES == 0:
        print("""
 _______
|       |
|
|
|
|
|""")
    if WRONG_GUESSES == 1:
        print("""
 _______
|       |
|       O
|
|
|
|""")
    if WRONG_GUESSES == 2:
        print("""
 _______
|       |
|       O
|       |
|
|
|""")
    if WRONG_GUESSES == 3:
        print("""
 _______
|       |
|       O
|      /|
|
|
|""")
    if WRONG_GUESSES == 4:
        print("""
 _______
|       |
|       O
|      /|\\
|
|
|""")
    if WRONG_GUESSES == 5:
        print("""
 _______
|       |
|       O
|      /|\\
|      /
|
|""")
    if WRONG_GUESSES == 6:
        print("""
 _______
|       |
|       O
|      /|\\
|      / \\
|
|""")

    return ""

def clear():
    print("\n" * 40)
    return ""

word_list = list(english_words_lower_alpha_set)
WORD = ""

def get_WORD():
    global DIFWORD
    global WORD
    WORD = random.choice(word_list)

    if not 10 > len(WORD) >= 5 or " " in WORD:
        DIFWORD = True
    while DIFWORD:
        WORD = random.choice(word_list)
        if " " in WORD:
            WORD.random.choice(word_list)
        elif 10 > len(WORD) >= 5:
            DIFWORD = False


print("""
  ('-. .-.   ('-.         .-') _            _   .-')      ('-.         .-') _
( OO )  /  ( OO ).-.    ( OO ) )          ( '.( OO )_   ( OO ).-.    ( OO ) )
,--. ,--.  / . --. /,--./ ,--,'  ,----.    ,--.   ,--.) / . --. /,--./ ,--,'
|  | |  |  | \\-.  \\ |   \\ |  |\\ '  .-./-') |   `.'   |  | \\-.  \\ |   \\ |  |\\
|   .|  |.-'-'  |  ||    \\|  | )|  |_( O- )|         |.-'-'  |  ||    \\|  | )
|       | \\| |_.'  ||  .     |/ |  | .--, \\|  |'.'|  | \\| |_.'  ||  .     |/
|  .-.  |  |  .-.  ||  |\\    | (|  | '. (_/|  |   |  |  |  .-.  ||  |\\    |
|  | |  |  |  | |  ||  | \\   |  |  '--'  | |  |   |  |  |  | |  ||  | \\   |
`--' `--'  `--' `--'`--'  `--'   `------'  `--'   `--'  `--' `--'`--'  `--'

(art from http://patorjk.com/software/taag/#p=display&h=1&v=1&f=Ghost&t=HANGMAN)
""")

while AGAIN:
    playagain = input("Play a game? (y/n)\n")
    playagain = playagain.lower()
    if playagain == "y":
        get_WORD()
        WRONG_GUESSES = 0
        HANGMAN = True
    elif playagain == "n":
        sys.exit()
    else:
        print("Please type y or n")


    while HANGMAN:
        HANG_WORD = len(WORD)* "_ "
        LETTERS_GUESSED = []

        GAME = True
        while GAME:



            if WRONG_GUESSES == 6:
                print(ascii_hangman())
                print("You lose :(")
                print(f"The WORD was {WORD}")

                GAME = False
                HANGMAN = False
                break

            elif "_" not in HANG_WORD:
                print("""

 7_O_/
  (/
  /\\/'
  7
 (art from http://www.ascii-art.de/ascii/s/stickman.txt by nico okha)
                    """)
                print("You win!")
                print(WORD)

                GAME = False
                HANGMAN = False
                break

            print(ascii_hangman())
            print(HANG_WORD)
            print(f"You have guessed {LETTERS_GUESSED} so far.")
            guess = input("Guess a letter \n")
            guess = guess.lower()

            if guess in illegal_guess:
                clear()
                print("Please choose a letter")

            else:
                if len(guess) > 1 or len(guess) == 0:
                    clear()
                    print("Please choose one letter.")

                if len(guess) == 1:
                    if guess not in LETTERS_GUESSED:
                        LETTERS_GUESSED += guess
                        if guess in WORD:
                            HANG_WORD = " ".join([x if x in LETTERS_GUESSED \
                            else "_" for x in WORD])
                            clear()
                            print("Correct!")

                        else:
                            clear()
                            print("Incorrect :(")
                            WRONG_GUESSES += 1


                    else:
                        clear()
                        print("Please choose a letter you haven't chosen")
