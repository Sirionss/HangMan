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

from random import  randrange
import os

clear = lambda: os.system('cls')
lines_str = '<' + '=' * 100 + '>\n\n' + '<' + '=' * 100 + '>\n'

wp_welcome_str = 'Hangman'.center(102, ' ')
wp_option1_str = '\n' + ' ' * 40 + '1. Start hangman'
wp_option2_str = ' ' * 40 + '2. Start hangman with custom wordlist'
wp_option3_str = ' ' * 40 + '3. Exit'
wp_option_number_input_str = '\nType a number of option:'

gpcus_welcome_str1 = 'Hangman Custom Mode\n'.center(102, ' ')
gpstn_welcome_str1 = 'Hangman Standart Mode\n'.center(102, ' ')
gp_welcome_str2 = 'Your guess should be a single letter'.center(102, ' ')
gpcus_hint1_input_str = '\nWrite a name fo the file with custom words:'
gp_hint2_input_str = ' ' * 40 + '\nWrite your guess:'
gp_incorrect_input1 = ' ' * 40 + 'This letter was already used'
gp_incorrect_input2 = ' ' * 40 + 'Incorrect format'

rp_gameover_str = 'Hahaha loooseer! Go try again!'.center(102, ' ')
rp_win_str = 'Congratulations, you won! You can try again!'.center(102, ' ')
rp_stats_str = 'Here is your statistics'
rp_choice1_str = '1. To welcome page'
rp_choice2_str = '2. Play standard mode'
rp_choice3_str = '3. Play custom mode'
rp_choice4_str = '4. Exit'
rp_option_number_input_str = '\nType a number of option:'
rp_stat1_str = 'The word was:'
rp_stat2_str = 'Count of mistakes: '
rp_stat3_str ='Count of correct guesses: '
rp_stat4_str = 'Percentage of correct answers over mistakes:'
def word_gen(wordlist):
    word = wordlist[randrange(len(wordlist))]
    word_dived = []
    for i in word:
        word_dived += i
    return word_dived

def custom_list_gen(file_name):
    wordlist = ''
    f = open(file_name, 'r')
    for line in f:
        wordlist += line.lower()
    wordlist = wordlist.split('\n')
    return wordlist

def welcome_page():
    clear()
    print(lines_str)
    print(wp_welcome_str)
    print(wp_option1_str)
    print(wp_option2_str)
    print(wp_option3_str)
    wp_choice = input(wp_option_number_input_str)
    if wp_choice == '1':
        game_page_stn_lst()
    elif wp_choice == '2':
        game_page_custom_lst()
    elif wp_choice == '3':
        return
    else:
        welcome_page()
    return

def game_page_custom_lst():
    clear()
    print(lines_str)
    print(gpcus_welcome_str1)
    print(gp_welcome_str2)
    file_name = input(gpcus_hint1_input_str)
    wordlist = custom_list_gen(file_name)
    word_divided_lst = word_gen(wordlist)
    word_guess_lst = []
    word_guess_str = ''
    for _ in word_divided_lst:
        word_guess_lst.append('_')
    for i in word_guess_lst:
        word_guess_str += i
    m_counter = 0
    c_counter = 0
    guesses_lst = []
    while m_counter < 10 and '_' in word_guess_lst:
        clear()
        print(lines_str)
        print(word_guess_str.center(102,' '))
        if guesses_lst:
            print(guesses_lst[-1])
        print(10 - m_counter, ' mistakes left')
        guess = input(gp_hint2_input_str)
        while len(guess) != 1 or guess == ' ' or guess in guesses_lst:
            if guess in guesses_lst:
                print(gp_incorrect_input1)
                guess = input(gp_hint2_input_str)
            else:
                print(gp_incorrect_input2)
                guess = input(gp_hint2_input_str)
        guess.lower()
        guesses_lst.append(guess)
        ind = 0 # index in word_guess_lst
        cor = 0 # number of correct guesses
        for k in word_divided_lst:
            if guess == k:
                word_guess_lst[ind] = k
                cor += 1
            ind += 1
        if cor == 0:
            m_counter += 1
            guesses_lst.append('Wrong Guess\n')
        else:
            c_counter +=1
            guesses_lst.append('Right Guess\n')
        word_guess_str = ''
        for i in word_guess_lst:
            word_guess_str += i

    results_page(word_divided_lst, guesses_lst, m_counter, c_counter)
    return

def game_page_stn_lst():
    clear()
    print(lines_str)
    print(gpstn_welcome_str1)
    print(gp_welcome_str2)
    input('Press enter to continue'.center(102,' '))
    wordlist = ['welcome', 'pickle','hangman','puppy','cat','psychology']
    word_divided_lst = word_gen(wordlist)
    word_guess_lst = []
    word_guess_str = ''
    for _ in word_divided_lst:
        word_guess_lst.append('_')
    for i in word_guess_lst:
        word_guess_str += i
    m_counter = 0
    c_counter = 0

    guesses_lst = []
    while m_counter < 10 and '_' in word_guess_lst:
        clear()
        print(lines_str)
        print(word_guess_str.center(102, ' '))
        if guesses_lst:
            print(guesses_lst[-1])
        print(10 - m_counter, ' mistakes left')
        guess = input(gp_hint2_input_str)
        while len(guess) != 1 or guess == ' ' or guess in guesses_lst:
            if guess in guesses_lst:
                print(gp_incorrect_input1)
                guess = input(gp_hint2_input_str)
            else:
                print(gp_incorrect_input2)
                guess = input(gp_hint2_input_str)
        guess.lower()
        guesses_lst.append(guess)
        ind = 0  # index in word_guess_lst
        cor = 0  # number of correct guesses
        for k in word_divided_lst:
            if guess == k:
                word_guess_lst[ind] = k
                cor += 1
            ind += 1
        if cor == 0:
            m_counter += 1
            guesses_lst.append('Wrong Guess\n')
        else:
            c_counter += 1
            guesses_lst.append('Right Guess\n')
        word_guess_str = ''
        for i in word_guess_lst:
            word_guess_str += i
    results_page(word_divided_lst,guesses_lst,m_counter,c_counter)
    return
def results_page(word_divided_lst,guesses_lst,m_counter,c_counter):
    clear()
    print(lines_str)
    if m_counter > 9:
        print(rp_gameover_str)
    else:
        print(rp_win_str)
    print(rp_stats_str)
    for k in guesses_lst:
        print(k, '',end='')
    word_guess_str = ''
    for i in word_divided_lst:
        word_guess_str += i
        rp_stat1_str
    print(rp_stat1_str,word_guess_str)
    print(rp_stat2_str,m_counter)
    print(rp_stat3_str, c_counter)
    print(rp_stat4_str, (c_counter*100//(c_counter+m_counter)) ,'%')
    print(rp_choice1_str)
    print(rp_choice2_str)
    print(rp_choice3_str)
    print(rp_choice4_str)
    rp_choice = input(rp_option_number_input_str)
    if rp_choice == '1':
        welcome_page()
    elif rp_choice == '2':
        game_page_stn_lst()
    elif rp_choice == '3':
        game_page_custom_lst()
    else:
        return
    return
welcome_page()


