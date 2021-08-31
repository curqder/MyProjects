"""
File: largest_digit.py
Name: 楊翔竣 Jim Yang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	Use recursion to find the answer
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: integer, > 0 or < 0
	:return: int, the biggest digit in n.
	this function will call the helper function.
	"""
	if n < 0:
		n *= -1  # make sure n > 0
		return helper(n, 0)
	else:
		return helper(n, 0)


def helper(n, largest):
	"""
	:param n: int,
	:param largest: int, to find the biggest digit
	:return: int, the biggest digit in n
	Because digit < 10, this function recursively check every digit of n
	"""
	remainder = n % 10
	if n < 10:  # Base case!
		if remainder > largest:
			return remainder
		else:
			return largest
	elif remainder > largest:  # Recursive
		largest = remainder
		return helper((n-remainder)//10, largest)
	else:  # Recursive
		return helper((n-remainder)//10, largest)



if __name__ == '__main__':
	main()
