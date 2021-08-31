"""
File: hangman.py
Name: 楊翔竣 Jim Yang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Create dashed words by random word() first.
    Then check inputting character is a single alpha or not.
    If user's input is correct, manipulate the string(hidden answer),
    makes dashed word(s) become un-dashed word(s), and keep the right word which has be guessed.
    When user guess all word, user win.
    If user's input is wrong, count wrong times, when wrong times equal to N_TURNS,
    user lose. Finally, show the answer.
    """
    ans = random_word()
    wrong_count = 0  # This variable shows wrong times user guessed
    hide_answer = guess(ans)  # This variable shows the string of dash word(s) and un-dashed word(s).
    while True:
        print('The world looks like: '+hide_answer)
        print('You have '+str(N_TURNS-wrong_count)+' guesses left.')
        input_ch = input('Your guess: ')
        while not input_ch.isalpha() or len(input_ch) != 1:  # Check until the character is a single alpha
            print('illegal format.')
            input_ch = input('Your guess: ')
        input_ch = input_ch.upper()  # case-insensitive
        ch = ''  # for the string manipulation
        if input_ch in ans:  # The guess is correct!
            print('You are correct!')
            for i in range(len(ans)):  # string manipulation
                if input_ch == ans[i]:
                    ch += input_ch
                elif hide_answer[i].isalpha():
                    ch += hide_answer[i]
                else:
                    ch += '-'
            hide_answer = ch  # re-assign(update) dashed words
            if hide_answer == ans:  # User win and end the game
                print('You win!!')
                break
        elif input_ch not in ans:  # The guess is un-correct
            wrong_count += 1
            print('There is no '+input_ch+"'s in the word.")
            if N_TURNS - wrong_count == 0:  # user has no chance anymore and lose the game
                print('You are completely hung : (')
                break
    print('The word was: '+ans)


def guess(s):
    """
    :param s: str, a random word
    :return: string with '-'
    This function create dash words.
    """
    ch = ''
    for i in range(len(s)):
        ch += '-'
    return ch


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
