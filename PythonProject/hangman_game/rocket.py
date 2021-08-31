"""
File: rocket.py
Name: 楊翔竣 Jim Yang
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


# This constant determines rocket size.
SIZE = 4


def main():
	"""
	Use double for loop to build function of the rocket's each part:
	head、belt、upper part、lower part
	(tail and head are same)
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	Separate left and right two parts by using (SIZE - J) condition.
	Draw left part with '/', and draw right part with '\'.
	"""
	for i in range(SIZE):  # the height (ROW)
		for j in range(2 * SIZE + 2):  # the width (COL)
			if i >= SIZE - j >= 0:  # the left part
				print('/', end='')
			elif 0 > SIZE - j >= -i-1:  # the right part
				print('\\', end='')
			else:
				print(' ', end='')  # blank area
		print('')


def belt():
	"""
	Use only one for loop.
	"""
	for i in range(2 * SIZE + 2):  # the width
		if i == 0:
			print('+', end='')
		elif i == 2*SIZE+1:
			print('+', end='')
		else:
			print('=', end='')
	print('')


def upper():
	"""
	First draw the two sides with '|',
	then separate left and right two parts by using (SIZE - J) condition.
	Check SIZE、(i+j) is even or odd in two part, then draw '\' or '/'.
	Draw other area with '.' .
	"""
	width = 2 * SIZE + 2  # This variable shows the height
	for i in range(SIZE):
		for j in range(width):
			v = i + j  # This variable shows (i + j) for later condition
			if j == 0:  # left side
				print('|', end='')
			elif j == width-1:  # right side
				print('|', end='')
			elif i >= SIZE - j >= 0:  # the left part
				if v % 2 == 0:  # v is even
					if SIZE % 2 == 0:  # SIZE is even
						print('/', end='')
					else:  # SIZE is odd
						print('\\', end='')
				else:  # v is odd
					if SIZE % 2 == 0:  # SIZE is even
						print('\\', end='')
					else:  # SIZE is odd
						print('/', end='')
			elif 0 > SIZE - j >= -i-1:  # the right part
				if v % 2 == 0:  # v is even
					if SIZE % 2 == 0:  # SIZE is even
						print('/', end='')
					else:  # SIZE is odd
						print('\\', end='')
				else:  # v is odd
					if SIZE % 2 == 0:  # SIZE is even
						print('\\', end='')
					else:  # SIZE is odd
						print('/', end='')
			else:
				print('.', end='')  # other area
		print('')


def lower():
	"""
	First draw the two side with '|',
	then separate left and right two parts by using
	(SIZE - 1 - i >= SIZE - j >= 0)、 (0 > SIZE - j >= -SIZE + i) conditions.
	Check (i+j) is even or odd in two part, then draw '\' or '/'.
	Draw other area with '.' .
	"""
	width = 2 * SIZE + 2  # This variable shows the height
	for i in range(SIZE):
		for j in range(width):
			v = i + j  # This variable shows (i + j) for later condition
			if j == 0:  # left side
				print('|', end='')
			elif j == width - 1:  # right side
				print('|', end='')
			elif SIZE - 1 - i >= SIZE - j >= 0:  # the left part
				if v % 2 == 0:  # v is even
					print('/', end='')
				else:  # v is odd
					print('\\', end='')
			elif 0 > SIZE - j >= -SIZE + i:  # the right part
				if v % 2 == 0:  # v is even
					print('/', end='')
				else:  # v is odd
					print('\\', end='')
			else:
				print('.', end='')  # other area
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()