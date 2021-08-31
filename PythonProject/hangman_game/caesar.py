"""
File: caesar.py
Name: 楊翔竣 Jim Yang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Use the inputting number to manipulate ALPHABET become new_alphabet.
    Then find the ciphered string's index in new_alphabet.
    Finally, use these indexes and ALPHABET to manipulate the result.
    """
    n = int(input('Secret number: '))
    cipher = input('What is ciphered string?: ')
    result = decipher(n, cipher)
    print('The deciphered string is: '+result)


def decipher(v, s):
    """
    :param v: int, shows how many times to produce shifted
    :param s: str, ciphered string which user inputted
    :return: The deciphered string
    The is function decipher the ciphered string.
    """
    s = s.upper()  # case-insensitive
    # Create a new alphabet sequence by the number user inputted
    new_alphabet = ALPHABET[len(ALPHABET)-v:] + ALPHABET[:len(ALPHABET)-v]
    ch = ''
    for i in range(len(s)):  # manipulate string by using indexes in new_alphabet
        j = new_alphabet.find(s[i])
        if j != -1:
            ch += ALPHABET[j]
        else:
            ch += s[i]
    return ch



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
