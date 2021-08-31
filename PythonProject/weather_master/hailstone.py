"""
File: hailstone.py
Name: 楊翔竣 Jim Yang
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Check n(variable) and re-assign repeatedly, until n == 1
    """
    print("This program computes Hailstone sequences.")
    n = int(input("Enter a number: "))
    s = 0  # This variable shows hom many steps to reach 1.
    while True:
        if n == 1:
            break
        if n % 2 == 1:  # n is odd
            v = int(3 * n + 1)  # This variable shows the new number.
            print(str(n)+" is odd, so I make 3n+1: "+str(v))
            n = v  # Re-assign
            s += 1
        if n % 2 == 0:  # n is even
            v = int(n / 2)
            print(str(n) + " is even, so I take half: " + str(v))
            n = v
            s += 1
    print("It took "+str(s)+" steps to reach 1.")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
