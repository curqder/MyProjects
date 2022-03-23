"""
File: boston_housing_competition.py
Name: Jim Yang 楊翔竣
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their 
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientist!
"""

import pandas as pd
from sklearn import preprocessing, linear_model, metrics, model_selection

TRAIN_FILE = 'boston_housing/train.csv'
TEST_FILE = 'boston_housing/test.csv'


def main():
	x_train = data_processing(TRAIN_FILE)
	train_data, val_data = model_selection.train_test_split(x_train, test_size=0.5)

	# True label
	y_train = train_data.pop('medv')
	y_val = val_data.pop('medv')

	# Polynomial Model
	poly_phi_extractor = preprocessing.PolynomialFeatures(degree=2)


	# Normalization / Standardization
	# standardization = preprocessing.StandardScaler()
	# x_train = standardization.fit_transform(x_train)

	# Model
	h = linear_model.LinearRegression()
	classifier = h.fit(train_data, y_train)

	# val test
	predictions = classifier.predict(train_data)
	print(metrics.mean_squared_error(predictions, y_train)**0.5)

	# Test dataset
	id, x_test = data_processing(TEST_FILE, mode='Test')
	predictions = h.predict(x_test)

	# output
	out_file(id, predictions, 'submission.csv')


def data_processing(filename, mode='Train'):
	data = pd.read_csv(filename)
	if mode == 'Train':
		data.pop('ID')
		return data
	else:
		id = data.pop('ID')
		return id, data


def out_file(id, predictions, filename):
	print('\n===============================================')
	print(f'Writing predictions to --> {filename}')
	with open(filename, 'w') as out:
		out.write('ID,medv\n')
		for i in range(len(predictions)):
			out.write(str(id.loc[i]) + ',' + str(predictions[i]) + '\n')
	print('===============================================')


if __name__ == '__main__':
	main()
