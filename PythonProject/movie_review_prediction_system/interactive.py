"""
File: interactive.py
Name: Jim Yang 楊翔竣
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""

from util import *
from submission import *


def main():
	weight = {}
	with open('weights', 'r', encoding='utf-8') as f:
		for line in f:
			weight[line.split()[0]] = float(line.split()[1])
	interactivePrompt(extractWordFeatures, weight)

	# interactivePrompt(extractWordFeatures, learnPredictor(readExamples('polarity.train'), readExamples('polarity.dev'),
# extractWordFeatures,numEpochs=40, alpha=0.01))
# test review:
# although this movie is suffers from some chiche , this film is still worth watching

if __name__ == '__main__':
	main()