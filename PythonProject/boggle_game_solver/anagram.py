"""
File: anagram.py
Name: 楊翔竣 Jim Yang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dictionary = []


def main():
    """
    Make an English dictionary as list(Global variable).
    Then use recursive function to find all anagrams which user input in dictionary.
    """
    ####################
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    start = 0
    end = 0
    while True:
        word = str(input('Find anagrams for: '))
        if word == EXIT:
            break
        else:
            start = time.time()
            print('Searching...')
            find_anagrams(word)
            end = time.time()
    ####################
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    :return: nothing
    This function read file and create a list in Global variable
    """
    global dictionary
    with open(FILE, 'r')as f:
        for line in f:
            dictionary.append(line.strip())


def find_anagrams(s):
    """
    :param s: str, user inputting word
    :return: nothing
    This function will call helper function to find and print all anagram.
    By turn s into a list of number(index).
    Finally, print all anagrams.
    """
    index_list = []
    ans_list = []
    for i in range(len(s)):
        index_list.append(int(i))
    find_anagrams_helper(s, index_list, [], ans_list)
    print(len(ans_list), 'anagrams:', ans_list)


def find_anagrams_helper(s, lst, current, ans_list):
    """
    :param s: str, original word user inputted
    :param lst: lst, be arranged to new order, which as a new word's digit order
    :param current: to find any possibly combination in anagram
    :param ans_list: lst, collect all anagrams
    :return: nothing
    Use recursion and backtracking to find anagrams.
    """
    ch = ''
    for index in current:  # turn number list into str
        ch += s[index]

    if len(s) == len(ch):  # Base case!
        if ch in dictionary:
            if ch in ans_list:
                pass
            else:
                ans_list.append(ch)
                print('Fond:', ch)
                print('Searching...')

    elif len(ch) != 0 and has_prefix(ch) is False:  # pruning
        pass

    else:
        for n in lst:  # number(index) list
            if n in current:
                pass  # already be used
            else:
                # choose
                current.append(n)
                # explore
                find_anagrams_helper(s, lst, current, ans_list)
                # un-choose
                current.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str, will be used to check
    :return:bol, True or false
    This function will check every word in dictionary, it will save time of algorithm.
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
