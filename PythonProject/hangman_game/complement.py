"""
File: complement.py
Name: 楊翔竣 Jim Yang
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Put DNA sequence(string) into build_complement(s) function,
    then return and print the result.
    """
    old_s = input("Please give me a DNA Strand an I'll find the complement: ")  # DNA sequence
    new_s = build_complement(old_s)
    print('The complement of '+old_s+' is '+new_s)


def build_complement(s):
    """
    :param s: str, inputted DNA sequence
    :return: str,the complement of s
    This function build the complement.
    """
    s = s.upper()  # case-insensitive
    new_s = ''
    for i in range(len(s)):  # string manipulation
        if s[i] == 'A':
            new_s += 'T'
        elif s[i] == 'T':
            new_s += 'A'
        elif s[i] == 'C':
            new_s += 'G'
        else:
            new_s += 'C'
    return new_s




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
