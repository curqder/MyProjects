"""
File: boggle.py
Name: Jim Yang 楊翔竣
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Put letters user inputted in Python list.
	Use Python list's index as coordinate, then use double for loop(find neighbors in 4*4 array)
	and recursive function to find all composed words in 'dictionary.txt'
	"""
	start = time.time()
	####################

	big_lst = []
	for i in range(1, 5):  # for user input
		print(i, end='')
		letters = input(' row of letters: ')
		cur_lst = list(ele.lower() for ele in letters.split())  # Case insensitive
		if len(letters) != 7 or len(cur_lst) != 4:
			print('Illegal input')
			break
		else:
			big_lst.append(cur_lst)  # there will be 4 small lists(cur_lst) in it

	ans = []  # answer list
	dictionary = read_dictionary()

	for i in range(4):
		for j in range(4):
			find_ans(big_lst, i, j, [big_lst[i][j]], ans, dictionary, [(i, j)])

	print('There are', len(ans), 'words in total.')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_ans(big_lst, i, j, cur_lst, ans, dictionary, coordinate):
	"""
	This recursive function find all composed words in 4*4 array
	:param big_lst: lst, original list of 4 small list
	:param i: int, index of big list
	:param j: int, index of small list
	:param cur_lst: list, current list of possible answer
	:param ans: lst, list of fond answers
	:param dictionary: list of "dictionary.txt"
	:param coordinate: tuple list, tuple is index of big list and index of small list, to save and avoid used letter
	:return: None
	"""
	cur_str = ''
	for ch in cur_lst:  # 串成字串
		cur_str += ch

	if len(cur_str) >= 4 and cur_str in dictionary:  # 查字典
		if cur_str not in ans:
			print('Found "'+cur_str+'"')
			ans.append(cur_str)

	for x in range(-1, 2, 1):  # -1、0、1
		for y in range(-1, 2, 1):  # -1、0、1
			horizon = i + x
			vertical = j + y
			if 0 <= horizon <= 3 and 0 <= vertical <= 3:
				if (horizon, vertical) not in coordinate:  # avoid used letter

					# choose
					ele = big_lst[horizon][vertical]
					cur_lst.append(ele)
					coordinate.append((horizon, vertical))

					# explore
					if has_prefix(cur_str):  # pruning
						find_ans(big_lst, horizon, vertical, cur_lst, ans, dictionary, coordinate)

					# un-choose
					cur_lst.pop()
					coordinate.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:return: list of "dictionary.txt"
	"""
	dictionary = []
	with open(FILE, 'r') as f:
		for line in f:
			dictionary.append(line.strip())
	return dictionary


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	dictionary = read_dictionary()
	for word in dictionary:
		if sub_s in word:
			return True
	return False


if __name__ == '__main__':
	main()
