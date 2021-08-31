"""
File: weather_master.py
Name: 楊翔竣 Jim Yang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This number controls when to stop
SENTINEL = -100


def main():
	"""
	Use a few variables to shows Highest temperature, Lowest temperature,Average,cold day(s).
	Check the first data user entered == SENTINEL,
	if not, continue the program.
	Then re-assign variables whenever user enter the next data.
	"""
	print("stanCode \"Weather Master 4.0\"!")
	data = int(input("Next Temperature: (or "+str(SENTINEL)+" to quit)? "))
	if data == SENTINEL:
		print("No temperatures were entered.")
	else:
		highest = data  # Highest temperature
		lowest = data  # Lowest temperature
		total = data  # The sum of temperatures user entered.
		number = 1  # shows how many times user has entered.
		avg = float(total / number)  # Average temperature
		cold = 0  # cold day(s)
		if data < 16:
			cold += 1
		while True:
			data = int(input("Next Temperature: (or "+str(SENTINEL)+" to quit)? "))
			if data == SENTINEL:
				break
			total += data
			number += 1
			avg = float(total / number)
			if data > highest:
				highest = data
			if data < lowest:
				lowest = data
			if data < 16:
				cold += 1
		print("Highest temperature = "+str(highest))
		print("Lowest temperature = "+str(lowest))
		print("Average = "+str(avg))
		print(str(cold)+" cold day(s)")




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
