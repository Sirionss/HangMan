#Project: Hangman
#
#Objective: Develop a text-based Hangman game that generates a hidden word and allows the player to guess letters to reveal the word.
#
#Requirements:
#
#    1. Word Selection:
#        a. Select a random word from a list of words.
#        b. Handle edge cases, such as words with repeating letters
#           or words that are too difficult or too easy.
#        c. Keep the selected word hidden from the player.
#    2. Guessing Mechanism:
#        a. Prompt the player to guess a letter.
#        b. Validate the player's input to ensure it is a single letter.
#        c. Check if the guessed letter is present in the hidden word.
#    3. Word Reveal:
#        a. Reveal the correct instances of the guessed letter in the hidden word.
#        b. Use blanks or underscores to represent the hidden word and the guessed letters.
#    4. Game Over:
#        a. End the game when the player guesses the entire hidden word correctly.
#        b. Display a congratulatory message and offer options to play again or exit.
#    5. Limited Attempts:
#        a. Set a limit on the number of incorrect guesses allowed.
#        b. If the player makes too many incorrect guesses, end the game and declare the player a loser.
#        c. Display a humorous message indicating the player's demise.
#    6. Gameplay Statistics:
#        a. Keep track of the player's correct guesses and incorrect guesses.
#        b. Provide post-game statistics, such as the number of guesses taken
#           and the percentage of correct guesses.
#    7. Customizable Word List:
#        a. Allow users to provide their own list of words for the game.
#        b. Handle file reading and parsing to load the custom word list.
#


from  tkinter import *
from random import  randrange


def wordgen(wordlist=None):

    if wordlist is None:
        wordlist = ['base', 'number', 'brain']
    word = wordlist[randrange(3)]
    word_dived = []
    for i in word:
        word_dived += i
    print(word_dived)
    return word_dived
def welcome_page():
    return
def game_page_stn_lst():
    print('') # smth to start with
def game_page_custom_lst():
    file_name = input()
    wordlist = ''
    f = open(file_name,'r')
    for line in f:
        wordlist += line
    wordlist = wordlist.split('\n')
    print(wordlist)
    word = wordgen(wordlist)
    print(word)
    word_guess = []
    for _ in word:
        word_guess += ' '
        print(word_guess)
    m_counter = 0
    print(word)
    while m_counter < 10:
        guess = input()
        while len(guess) != 1 or guess == ' ' :
            guess = input()
        i = 0
        m = 0
        for k in word:
            if guess == k:
                word_guess[i] = k + ' '
                m +=1
            i += 1
        if m == 0:
            m_counter +=1
        print(word_guess)

def results_page():
    return

root = Tk()
root.title('Hangman')
root.columnconfigure(0,weight = 1)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width // 2 - 250    #I use those variables to open the app in the center of monitor
y = screen_height // 2 - 300   # and I made this number a bit bigger so it would open a bit higher
root.geometry(f'500x500+{x}+{y}')
root.resizable(height= False) # Using this method I restricted resizing so there wouldn't be any errors
Label(root, text='================', font='Arial 20').grid( row=0, column=0, columnspan=2)
x = root.winfo_width()
print(x)


root.mainloop()

#wordgen()
#game_page_custom_lst()