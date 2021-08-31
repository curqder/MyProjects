"""
File: similarity.py
Name: 楊翔竣 Jim Yang
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Build a function which find the best match.
    By checking (len(long_sequences)-len(short_sequences)+1) times to find the max matched times.
    Each time will cut the long sequence into the same part of the short one, and manipulate string(the match).
    When find the max matched times, return the result(the best match).
    """
    long_sequence = str(input('Please give me a DNA sequence to search: '))
    short_sequence = str(input('What DNA sequence would you like to match? '))
    result = similarity(long_sequence, short_sequence)
    print('The best match is '+result)


def similarity(s1, s2):
    """
    :param s1: str, long DNA sequence
    :param s2: str, short DNA sequence
    :return: str, the best matched part form s1
    The is function find the best match.
    """
    s1 = s1.upper()  # case-insensitive
    s2 = s2.upper()
    if s2 in s1:
        return s2  # shows 100% match
    else:
        max_count = 0  # This variable shows the max matched times
        result = ''
        for i in range(len(s1)-len(s2)+1):  # To check (len(s1)-len(s2)+1) times
            ch = ''
            match_count = 0  # Shows how many matches in each time
            cut_s1 = s1[i:i+len(s2)]  # Cut the long sequence from i into the same part of the short one
            for j in range(len(s2)):  # Check two sequences(same length)
                if cut_s1[j] == s2[j]:  # Count how many matches and manipulate string(the match)
                    match_count += 1
                    ch += s2[j]  # build the matched part
                else:
                    ch += cut_s1[j]  # build the un-matched part
            if match_count > max_count:  # Check if find the best match
                max_count = match_count  # re-assign the max matched times
                result = ch  # re-assign the best match
        return result


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
