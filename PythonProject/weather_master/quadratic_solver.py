"""
File: quadratic_solver.py
Name: 楊翔竣 Jim Yang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Check discriminant first,then compute the x's root.
	"""
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	d = int(b * b - 4 * a * c)  # This variable shows the discriminant
	if d < 0:
		print("No real roots")
	elif d == 0:
		y = math.sqrt(d)  # When d >= 0, this function works
		root = float((-b + y) / 2 * a)
		print("One root: "+str(root))
	else:  # d > 0
		y = math.sqrt(d)  # When d >= 0, this function works
		root1 = float((-b + y) / 2 * a)
		root2 = float((-b - y) / 2 * a)
		print("Two roots: "+str(root1)+" , "+str(root2))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
